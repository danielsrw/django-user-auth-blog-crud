from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Tag, Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
