from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random

class UserManager(BaseUserManager):
    def create_user(self,phone,password=None,**extra_fields):

        if not phone:
            raise ValueError('User must have a phone')
        user = self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user
    def create_superuser(self,phone,password=None,**extra_fields):

        if not phone:
            raise ValueError('User must have a phone')
        user = self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff   = True
        user.save(using=self._db)
        return user


class Restaurant(models.Model):
    creator_name = models.CharField(max_length=150,null=True)
    restaurant_name = models.CharField(max_length=150,null=True)
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=200,null=True)
    district = models.CharField(max_length=150,null=True)
    state = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=300,null=True)

    def __str__(self):
        return str(self.restaurant_name)


class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True,null=True)
    phone = models.CharField(max_length=20,unique=True)
    restaurant = models.ForeignKey(Restaurant , on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD='phone'

class DefaultCats(models.Model):
    no = models.CharField(max_length=15,null=True)
    image = models.FileField(upload_to="defaultcatagory", null=True)

    def __str__(self):
        return str(self.no)

class Category(models.Model):
    restaurent = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30,null=True)
    icon = models.FileField(upload_to="catagory", null=True)

    def __str__(self):
        return str(self.name)


class RestaurantQrcode(models.Model):
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE,null=True)
    resto_url = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='qrcode',blank=True)
    

    def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.resto_url)
      canvas=Image.new("RGB", (800,800),"white")
    #   draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)

    def __str__(self):
        return str(self.restaurant)