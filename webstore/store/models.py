from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

'''
class Cart(models.Model):
    user = ?
    product = models.ManyToManyField(Product)
    
    
cart = Cart()
total_products_in_cart = cart.products.objects.all.count()
'''