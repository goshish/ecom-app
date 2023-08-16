from django.urls import path
from . import views
from .views import Main, RegisterFormView, LoginUserView, LogoutView



urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('cart/', views.cart, name='cart'),
    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('checkout', views.checkout, name='checkout'),
    path('add_to_cart/<int:pizza_id>/', views.AddToCart, name='add-cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('success/', views.success_view, name='success'),
    path('cancel/', views.cancel_view, name='cancel')
]
