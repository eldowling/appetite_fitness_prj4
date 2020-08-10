# Generated by Django 3.0.7 on 2020-08-09 08:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200806_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(default=datetime.datetime(2020, 8, 9, 8, 26, 12, 355915, tzinfo=utc), max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product_subscription',
            name='code',
            field=models.CharField(default=datetime.datetime(2020, 8, 9, 8, 26, 12, 357135, tzinfo=utc), max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='sizes',
            name='code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subscription_type',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
