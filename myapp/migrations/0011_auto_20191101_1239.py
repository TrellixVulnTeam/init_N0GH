# Generated by Django 2.2.6 on 2019-11-01 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_item_discount_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]
