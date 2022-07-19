from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_-=+/.,<>`~|{}[]')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    length = int(request.GET.get('length'))

    password = ''

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})
