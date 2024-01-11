from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Category, Tag

def home(request):
	return render(request, 'index.html')

def blog(request):
	categories = Category.objects.all()[0:3]
	tags = Tag.objects.all()[0:3]
	context = {
		'categories': categories,
		'tags': tags,
	}

	return render(request, 'blog.html', context)

def blogSingle(request):
	categories = Category.objects.all()[0:3]
	tags = Tag.objects.all()[0:3]
	context = {
		'categories': categories,
		'tags': tags,
	}

	return render(request, 'show-blog.html', context)

def signUp(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})

def profile(request):
	return render(request, 'profile.html')