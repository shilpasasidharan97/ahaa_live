# Generated by Django 4.1.3 on 2022-11-23 08:32

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("website", "0006_frontbanner_productpagebanner")]

    operations = [migrations.AddField(model_name="product", name="is_available", field=models.BooleanField(default=True))]