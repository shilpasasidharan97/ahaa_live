# Generated by Django 4.1.3 on 2022-11-21 06:20

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("website", "0002_cart_cartitems")]

    operations = [migrations.AlterField(model_name="cartitems", name="quantity", field=models.IntegerField(default=1, null=True))]