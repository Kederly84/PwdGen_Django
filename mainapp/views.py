import random
import string
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'mainapp/home.html')


def password(request):
    length = int(request.GET.get('length', 10))
    characters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    if request.GET.get('Uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('numbers'):
        characters.extend([str(x) for x in range(10)])
    if request.GET.get('Special'):
        characters.extend(string.punctuation)
    pwd = ''
    for x in range(length):
        pwd += random.choice(characters)
    return render(request, 'mainapp/password.html', {'password': pwd})


def description(request):
    return render(request, 'mainapp/description.html')
