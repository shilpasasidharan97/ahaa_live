# Generated by Django 4.1.3 on 2022-12-12 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('icon', models.FileField(null=True, upload_to='catagory')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='DefaultCats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=15, null=True)),
                ('image', models.FileField(null=True, upload_to='defaultcatagory')),
            ],
            options={
                'verbose_name_plural': 'Default Categories',
            },
        ),
        migrations.CreateModel(
            name='FrontBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='front-banner')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPageBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='Product-banner')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(max_length=150, null=True)),
                ('restaurant_name', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('district', models.CharField(max_length=150, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('is_table', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurant',
            },
        ),
        migrations.CreateModel(
            name='RestoSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session_id', models.CharField(max_length=200, null=True)),
                ('resto_pk', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='video')),
            ],
            options={
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.category')),
            ],
            options={
                'verbose_name_plural': 'SubCategory',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=2000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=2000, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=2000, null=True)),
                ('location', models.CharField(blank=True, max_length=2000, null=True)),
                ('resturant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestoBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='Resturant-banner')),
                ('resto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantQrcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resto_url', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='qrcode')),
                ('restaurant', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('ingrediants', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='products')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('is_available', models.BooleanField(default=True)),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.subcategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='restaurent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant'),
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.cart')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
            options={
                'verbose_name_plural': 'Cart Items',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
