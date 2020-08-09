
from django.urls import path
from . import views
from .views import ProductDetailView, CartView


urlpatterns = [
    path('index.html', views.home_view, name='home'),
    path('shop.html', views.shop_view, name='shop'),
    path('product_details/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('contact.html', views.contact_view, name='contact'),
    path('login.html', views.login_view, name='login'),
    path('cart.html', CartView.as_view(), name='cart'),
    path('checkout.html', views.checkout_view, name='checkout'),
    path('confirmation.html', views.confirmation_view, name='confirmation'),
]
