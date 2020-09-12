from django.db import models
from django.utils import timezone

from profiles.models import UserProfile
from products.models import Product


class Discussions(models.Model):

    class Meta:
        verbose_name_plural = 'Discussions'
    
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='discussions')
    product = models.ForeignKey(Product, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    topic = models.CharField(max_length=254, null=False, blank=False)
    disc_topic_text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateField(default=timezone.now, editable=False)
    modified = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Discussion_Comments(models.Model):

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='discussion_comments')
    disc_topic = models.ForeignKey(Discussions, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    comment = models.TextField()
    created = models.DateField(default=timezone.now, editable=False)
    modified = models.DateField(default=timezone.now)

    def __str__(self):
        return self.disc_topic
