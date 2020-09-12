from django.contrib import admin
from .models import Discussions, Discussion_Comments


class DiscussionsAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'product',
        'topic',
        'image',
        'created',
        'modified',
    )

    ordering = ('product', 'created', 'user_profile',)


class Discussion_CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'disc_topic',
        'created',
        'modified',
    )

    ordering = ('created',)
