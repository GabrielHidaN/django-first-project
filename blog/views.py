#from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index_blog(request):

    return render(
        request , 
        'blog/index.html'
    )

def whoami(request):

    return render(
        request,
        'blog/whoami.html'
    )

def portifolio(request):

    return render(
        request , 
        'blog/portifolio.html'
    )
