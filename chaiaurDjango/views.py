from django.http import HttpResponse
from django.shortcuts import render


def home(request):
  # return HttpResponse("Hello, world. You are at chai aur Django Home page")
  return render(request, 'website/home.html')

def about(request):
  return HttpResponse("Hello, world. You are at chai aur Django About page")

def contact(request):
  return HttpResponse("Hello, world. You are at chai aur Django contact page")

def location(request):
  return HttpResponse("Hello. world. You are at Chai aur Django Location page")