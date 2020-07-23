
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop.html', views.shop_view, name='shop'),
]
