# Generated by Django 4.1.3 on 2022-11-25 11:52

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("website", "0007_product_is_available")]

    operations = [
        migrations.CreateModel(
            name="RestoSave",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_session_id", models.CharField(max_length=200, null=True)),
                ("resto_pk", models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterModelOptions(name="cartitems", options={"verbose_name_plural": "Cart Items"}),
        migrations.AlterModelOptions(name="category", options={"verbose_name_plural": "Categories"}),
        migrations.AlterModelOptions(name="defaultcats", options={"verbose_name_plural": "Default Categories"}),
        migrations.AlterModelOptions(name="product", options={"verbose_name_plural": "Products"}),
        migrations.AlterModelOptions(name="restaurant", options={"verbose_name_plural": "Restaurant"}),
        migrations.AlterModelOptions(name="subcategory", options={"verbose_name_plural": "SubCategory"}),
    ]