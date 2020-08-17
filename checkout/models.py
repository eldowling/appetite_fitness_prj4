import uuid

from django.db import models
from django.db.models import Sum, Q
from django.conf import settings

from products.models import Product, Product_Subscription, Sizes


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    non_delivery_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        # Order total is for items that need to be delivered
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # Non_delivery_total is for online / live subscriptions that don't need a delivery charge
        self.non_delivery_total = self.lineitems.aggregate(
            Sum('lineitem_nondel_total'))['lineitem_nondel_total__sum'] or 0
        # delivery_cost is only calculated for deliverable items
        # but checked against free delivery threshold for the order_subtotal value
        order_subtotal = self.order_total + self.non_delivery_total
        if order_subtotal < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.lineitems.aggregate(
                Sum('lineitem_deliverycost'))['lineitem_deliverycost__sum'] or 0
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.non_delivery_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_subscription = models.ForeignKey(Product_Subscription, null=True, blank=True,
                                on_delete=models.SET_NULL)
    product_size = models.ForeignKey(Sizes, null=True, blank=True,
                                on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    delivery_charge = models.BooleanField(default=False, null=True, blank=True)
    lineitem_deliverycost = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
    lineitem_nondel_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """

        self.delivery_charge = self.product_subscription.delivery_charge
        # Check if there is a delivery charge for the subscription type of item selected
        # and calculate the delivery cost if it is a deliverable item
        if self.delivery_charge:
            self.lineitem_total = self.product_subscription.price * self.quantity
            sdp = settings.STANDARD_DELIVERY_PERCENTAGE
            self.lineitem_deliverycost = self.lineitem_total * sdp / 100
        else:
            self.lineitem_total = 0
            self.lineitem_nondel_total = self.product_subscription.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product_code {self.product.code} on order {self.order.order_number}'

class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    code = models.CharField(max_length=4)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name