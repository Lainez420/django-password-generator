from django.shortcuts import render
from django.http import HttpResponse
import random

def about(request):
    return render(request, 'About.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))
   
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!¡¿?/()%#@'))

    if request.GET.get('number'):
        characters.extend(list('123456789'))

    for x in range(length):
        generated_password += random.choice(characters)
    return render(request, 'password.html', {'password':generated_password})
# Create your views here.
