from .forms import UserForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import User


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ Sanity Check</h1>')


def about(request):
    return render(request, 'about.html')


def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/index.html', context)
