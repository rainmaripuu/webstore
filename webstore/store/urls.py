
from django.urls import path
from . import views
from .views import ProductDetailView, CartView, CreateProductView, ProductListView, UpdateProductView, DeleteProductView
from .views import PurchaseSuccessView #, ProfileView

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
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('checkout.html', views.checkout_view, name='checkout'),
    path('confirmation.html', views.confirmation_view, name='confirmation'),
    path('admin.html', views.admin_view, name='admin'),
    path('signup.html', views.signup, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('update_profile/', views.update_profile_view, name='update_profile'),
#    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('purchase_success.html', PurchaseSuccessView.as_view(), name='purchase_success'),
]
