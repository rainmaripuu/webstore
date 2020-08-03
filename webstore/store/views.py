from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def home_view(request):
    return render(request, 'index.html', {})


def shop_view(request):
    item = Product.objects.all()
    context = {'products': item}
    return render(request, 'shop.html', context)


def details_view(request):
    return render(request, 'product_details.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})


def login_view(request):
    return render(request, 'login.html', {})


def cart_view(request):
    return render(request, 'cart.html', {})


def checkout_view(request):
    return render(request, 'checkout.html', {})


def confirmation_view(request):
    return render(request, 'confirmation.html', {})