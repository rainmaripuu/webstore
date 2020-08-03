
from django.urls import path
from . import views



urlpatterns = [
    path('index.html', views.home_view, name='home'),
    path('shop.html', views.shop_view, name='shop'),
    path('product_details.html', views.details_view, name='details'),
    path('contact.html', views.contact_view, name='contact'),
    path('login.html', views.login_view, name='login'),
    path('cart.html', views.cart_view, name='cart'),
    path('checkout.html', views.checkout_view, name='checkout'),
    path('confirmation.html', views.confirmation_view, name='confirmation'),
]
