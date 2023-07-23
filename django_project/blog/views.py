from django.shortcuts import render,redirect, get_object_or_404  #* rendering
from django.urls import reverse
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
# !Create your views here.
def home(request):
    #* creating context
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted'] # - for reverse order
    paginate_by = 5
    
class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostCreateView(LoginRequiredMixin, CreateView): #! Mixins before Views
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # def get_absolute_url():
    # success_url

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #! Mixins before Views
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # def get_absolute_url():
    # success_url
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Userr Posts
class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    #! Will be overwritten from queryset
    # ordering = ['-date_posted'] # - for reverse order 
    paginate_by = 5
    
    def get_queryset(self):
        # super().get_queryset()
        user  = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')