from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView
from .forms import RegisterUserForm, AuthenticationForm, AddToCartForm
from .models import *
from django.conf import settings
from pizzeria.settings import STRIPE_SECRET_KEY
import stripe
import os



stripe.api_key = STRIPE_SECRET_KEY

class Main(ListView):
    model = Pizza
    template_name = 'main/index.html'
    context_object_name = 'pizza'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_to_cart_form'] = AddToCartForm()
        return context

    def get_queryset(self):
        return Pizza.objects.all()


class RegisterFormView(CreateView):
    form_class = RegisterUserForm
    model = User
    success_url = reverse_lazy('login')
    template_name = 'main/registration.html'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    success_url = ''

    def form_valid(self, form):
        return super().form_valid(form)


def cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.price for item in cart_items)
    return render(request, 'main/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    line_items = []

    for cart_item in cart_items:
        pizza = cart_item.pizza
        line_item = {
            'price_data': {
                'currency': 'usd',
                'unit_amount': pizza.price * 100,
                'product_data': {
                    'name': pizza.title,
                },
            },
            'quantity': cart_item.quantity,
        }
        line_items.append(line_item)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=os.getenv('success_url'),
        cancel_url=os.getenv('cancel_url')
    )

    return redirect(checkout_session.url)



def success_view(request):
    return render(request, 'main/success.html')

def cancel_view(request):
    return render(request, 'main/cancel.html')

@login_required
def AddToCart(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart, _ = Cart.objects.get_or_create(user=request.user)
            price = pizza.price * cd['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza, defaults={'price': price})
            if not created:
                cart_item.quantity += cd['quantity']
                cart_item.price += price
                cart_item.save()
            return redirect('cart')
    else:
        form = AddToCartForm()

    return render(request, 'main/index.html', {'pizza': pizza, 'add_to_cart_form': form})


@login_required
def clear_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.cartitem_set.all().delete()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')








