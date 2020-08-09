from django.db import models
from django.contrib.auth.models import AbstractUser
from store.constants import COUNTRIES
import os

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('products', str(instance.id), filename)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    img = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name


class StoreUser(AbstractUser):
    COMMUNICATION_CHOICES = [('email', 'Email'), ('sms', 'SMS')]
    country = models.CharField(max_length=50, null=True, blank=True, choices=COUNTRIES)
    city = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    preferred_communication = models.CharField(max_length=50, null=True, blank=True, choices=COMMUNICATION_CHOICES)

'''
class CartItem(models.Model): #trackib mitu itemit on korvis
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
'''


class Cart(models.Model):
    user = models.ForeignKey(
        StoreUser, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True) #kui sooritab ostu, siis peaks muutma active-i Falseks
    product = models.ManyToManyField(Product)

    

# cart = Cart()
# total_products_in_cart = cart.products.objects.all.count()
