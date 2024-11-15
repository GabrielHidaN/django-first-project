#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_blog(request):
    print('Blog')
    return HttpResponse('Blog do App 1')

def whoami(request):
    print('whoami')
    return HttpResponse('Whoami')

def portifolio(request):
    print('Portifolio')
    return HttpResponse('Portifolio')