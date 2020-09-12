from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from profiles.models import UserProfile
import uuid


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Subscription_Type(models.Model):

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name


class Sizes(models.Model):

    class Meta:
        verbose_name_plural = 'Sizes'

    code = models.CharField(max_length=4)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Colour(models.Model):

    code = models.CharField(max_length=4)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    code = models.CharField(max_length=40, default = uuid.uuid4, null=False, blank=False, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    subscription = models.BooleanField(default=False, null=True, blank=True)
    product_sub = models.ManyToManyField('Product_Subscription', through='Subscriptions')
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    colour = models.ForeignKey('Colour', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name

    def get_avg_rating(self):
        """Gets the rating from the user reviews of a product to calculate and
           display an average rating for each product"""
           # This function was created with assistance from Malia Havlicek in Code Institute,
           # who guided me to learn the aggregate function in Django, and how it can be used
           # to display an Average from the user_ratings field
        try:
            # Calculate the average rating for the product based on Reviews.user_rating
            rating = Reviews.objects.filter(product=self.pk).aggregate(Avg('user_rating'))
            rating = rating['user_rating__avg']
        except:
            rating = 0
        return rating

class Product_Subscription(models.Model):

    code = models.CharField(max_length=40, default=uuid.uuid4, null=False, blank=False, unique=True)
    name = models.CharField(max_length=254)
    subscription_type = models.ForeignKey('Subscription_Type', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    size = models.ForeignKey('Sizes', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    quantity_available = models.DecimalField(max_digits=6, decimal_places=0, null=True,
                                 blank=True)
    delivery_charge = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Subscriptions(models.Model):

    class Meta:
        verbose_name_plural = 'Subscriptions'

    code = models.CharField(max_length=40, default=uuid.uuid4, null=False, blank=False, unique=True)
    product = models.ForeignKey('Product', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_sub = models.ForeignKey('Product_Subscription', null=True, blank=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name


class Reviews(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    product = models.ForeignKey('Product', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=254, null=False, blank=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='reviews')
    user_rating = models.DecimalField(
        default=1,
        max_digits=3,
        decimal_places=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    created = models.DateTimeField(editable=False)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Reviews, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_product(self):
        return self.product

    def get_user(self):
        return self.user

