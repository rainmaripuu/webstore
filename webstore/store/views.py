from django.shortcuts import render
from .models import Product, Category
from django.views.generic import DetailView

# Create your views here.


def home_view(request):
    newest = Product.objects.order_by('-added_date')
    context = {'newest': newest[0:3]}
    return render(request, 'index.html', context)


def filter_context(filter_val, shop_context):
    shop_context = Product.objects.filter(name__icontains=filter_val) | \
        shop_context.filter(category__name__icontains=filter_val)
    return shop_context


def shop_view(request):
    item = Product.objects.all()
    filter_val = request.GET.get('filter', None)
    newest = Product.objects.order_by('-added_date')
    if filter_val:
        newest = Product.objects.filter(name__icontains=filter_val) | \
            newest.filter(category__name__icontains=filter_val)
    price_high_low = Product.objects.order_by('-price')
    if filter_val:
        price_high_low = Product.objects.filter(name__icontains=filter_val) | \
            price_high_low.filter(category__name__icontains=filter_val)
    price_low_high = Product.objects.order_by('price')
    if filter_val:
        price_low_high = Product.objects.filter(name__icontains=filter_val) | \
            price_low_high.filter(category__name__icontains=filter_val)
    context = {'products': item, 'newest': newest, 'price_high_low': price_high_low, 'price_low_high': price_low_high}
    context['orderby'] = request.GET.get('orderby', 'newest')
    context['filter'] = request.GET.get('filter', None)
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