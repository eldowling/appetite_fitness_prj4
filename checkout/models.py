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
        #self.order_total = self.lineitems.aggregate(delivery_charge=True(
        #    Sum('lineitem_total')))['lineitem_total__sum'] or 0            
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0            
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            sdp = settings.STANDARD_DELIVERY_PERCENTAGE
            self.delivery_cost = self.order_total * sdp / 100
        else:
            self.delivery_cost = 0
            
        #if self.product_subscription.delivery_charge:
        #    self.non_delivery_total = self.lineitems.aggregate(delivery_charge=True(
        #        Sum('lineitem_total')))['lineitem_total__sum'] or 0
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
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product_subscription.price * self.quantity
        self.delivery_charge = self.product_subscription.delivery_charge
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product_code {self.product.code} on order {self.order.order_number}'