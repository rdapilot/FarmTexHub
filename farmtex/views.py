from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'farmtex/index.html')#HttpResponse("<h1>Hello, world. You're at my home page.</h1>")

def user(request):
    return render(request, 'farmtex/user.html')#HttpResponse("<h1>Hello, world. You're at my home page.</h1>")

def icons(request):
    return render(request, 'farmtex/icons.html')#HttpResponse("<h1>Hello, world. You're at my home page.</h1>")