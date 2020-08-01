
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop.html', views.shop_view, name='shop'),
    path('product_details.html', views.details_view, name='details'),
    path('contact.html', views.contact_view, name='contact'),
]
