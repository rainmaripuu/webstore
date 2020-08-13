from django.shortcuts import render
from .models import Product, Category, Cart
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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


class CartView(ListView):
    model = Product
    template_name = 'cart.html'
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user
        cart = Cart.objects.filter(user=user).filter(active=True).first()
        if cart == None:
            self.products = []
        else:
            self.products = cart.products.all()
        return self.products

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        total = 0

        # if len(self.products) == 0:
        #     context('no_products') = True

        for p in self.products:
            total += p.price
        context['total'] = total
        return context

# def details_view(request):
#     return render(request, 'product_details.html', {})


class ProductListView(ListView):
    model = Product
    template_name = 'list.html'
    context_object_name = 'products'


class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('list')


class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('list')


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    permission_required = ['products.delete_product', ]
    model = Product
    template_name = 'delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('list')


def contact_view(request):
    return render(request, 'contact.html', {})


# def login_view(request):
#     return render(request, 'login.html', {})


@login_required
def admin_view(request):
    return render(request, 'admin.html', {})
# def cart_view(request):
#     return render(request, 'cart.html', {})


def checkout_view(request):
    return render(request, 'checkout.html', {})


def confirmation_view(request):
    return render(request, 'confirmation.html', {})