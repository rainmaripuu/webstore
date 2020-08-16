from django.contrib import admin
from store.models import Product, Category, StoreUser, Cart
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

admin.site.register(Product)
admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(StoreUser)
admin.site.register(Cart)
