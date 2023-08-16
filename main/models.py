from django.contrib.auth.models import User
from django.db import models


class Pizza(models.Model):
    title = models.CharField(max_length=20, verbose_name='Pizza name')
    content = models.TextField(max_length=70, blank=True, verbose_name='Description')
    weight = models.IntegerField(blank=True, verbose_name='Weight')
    price = models.IntegerField(blank=True, verbose_name='Price')
    photo = models.ImageField(blank=True, upload_to="photos/%y/%m/%d/")
    stripe = models.CharField(default=None, max_length=100, verbose_name='Stripe ID', blank=True, null=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Pizza, through='CartItem', related_name='carts')

    def add(self, pizza, price, quantity):
        cart_item, created = CartItem.objects.get_or_create(cart=self, pizza=pizza)
        cart_item.price = price
        cart_item.quantity = quantity
        cart_item.save()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
