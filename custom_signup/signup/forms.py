from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'favorite_color', 'bio',
                  'is_active', 'password1', 'password2')
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2',)
