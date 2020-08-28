from django.shortcuts import render, redirect
from .models import Product, Category, Cart, StoreUser
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from .forms import SignUpForm, UpdateUserForm


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            new_user = StoreUser.objects.create_user(username=username, password=raw_password)
            new_user.save()
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def contact_view(request):
    return render(request, 'contact.html', {})


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def update_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateUserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'update_profile.html', {'form': form})

# class ProfileView(DetailView):
#     model = StoreUser
#     template_name = 'profile.html'
#     context_object_name = 'user'


@login_required
def admin_view(request):
    return render(request, 'admin.html', {})
# def cart_view(request):
#     return render(request, 'cart.html', {})


def checkout_view(request):
    return render(request, 'checkout.html', {})


def confirmation_view(request):
    return render(request, 'confirmation.html', {})


@login_required
def add_to_cart(request, product_id):
    user = request.user
    carts = Cart.objects.filter(user=user).filter(active=True)
    user_cart = None
    if carts.count() == 0:
        new_cart = Cart.objects.create(user=user)
        new_cart.save()
        user_cart = new_cart
    else:
        user_cart = carts.first()

    product = Product.objects.filter(id=product_id).first()

    user_cart.products.add(product)

    return HttpResponseRedirect(reverse_lazy('cart'))


@login_required
def purchase_view(request):
    user = request.user
    user_cart = Cart.objects.filter(user=user).filter(active=True).first()
    user_products = user_cart.products.all()

    for product in user_products:
        product.quantity = product.quantity -1
        product.save()

    user_cart.active = False
    user_cart.save()

    return HttpResponseRedirect(reverse_lazy('purchase_success'))


class PurchaseSuccessView(TemplateView):
    template_name = 'purchase_success.html'