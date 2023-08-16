from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'reg-user'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'reg-user'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'reg-user'}))


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'quantity-input'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

