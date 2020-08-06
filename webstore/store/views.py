from django.shortcuts import render
from .models import Product, Category
from django.views.generic import DetailView

# Create your views here.


def home_view(request):
    newest = Product.objects.order_by('-added_date')
    context = {'newest': newest[0:3]}
    return render(request, 'index.html', context)


def shop_view(request):
    item = Product.objects.all()
    newest = Product.objects.order_by('-added_date')
    price_high_low = Product.objects.order_by('-price')
    price_low_high = Product.objects.order_by('price')
    context = {'products': item, 'newest': newest, 'price_high_low': price_high_low, 'price_low_high': price_low_high}

    return render(request, 'shop.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


# def details_view(request):
#     return render(request, 'product_details.html', {})


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