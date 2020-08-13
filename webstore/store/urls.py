
from django.urls import path
from . import views
from .views import ProductDetailView, CartView, CreateProductView, ProductListView, UpdateProductView, DeleteProductView


urlpatterns = [
    path('index.html', views.home_view, name='home'),
    path('shop.html', views.shop_view, name='shop'),
    path('list.html', ProductListView.as_view(), name='list'),
    path('create.html', CreateProductView.as_view(), name='create'),
    path('product_details/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete'),
    path('contact.html', views.contact_view, name='contact'),
    # path('login.html', views.login_view, name='login'),
    path('cart.html', CartView.as_view(), name='cart'),
    path('checkout.html', views.checkout_view, name='checkout'),
    path('confirmation.html', views.confirmation_view, name='confirmation'),
    path('admin.html', views.admin_view, name='admin'),
]
