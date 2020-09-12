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
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic

    def get_topic(self):
        return self.topic

    def get_name(self):
        if self.user_profile:
            return self.user_profile.user.get_full_name()
        return None


class Discussion_Comments(models.Model):

    class Meta:
        verbose_name_plural = 'Discussion Comments'

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='discussion_comments')
    disc_topic = models.ForeignKey(Discussions, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    comment = models.TextField()
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.disc_topic.topic

    def get_name(self):
        if self.user_profile:
            return self.user_profile.user.get_full_name()
        return None
