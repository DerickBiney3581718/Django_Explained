from django.shortcuts import render   #* rendering
from django.http import HttpResponse
from .models import Post
# !Create your views here.
def home(request):
    #* creating context
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

