# Generated by Django 4.1.3 on 2022-11-26 04:29

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("website", "0008_restosave_alter_cartitems_options_and_more")]

    operations = [
        migrations.CreateModel(
            name="RestoBanner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.FileField(blank=True, null=True, upload_to="Resturant-banner")),
            ],
        )
    ]