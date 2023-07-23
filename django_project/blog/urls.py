from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(template_name = 'blog/home.html'), name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name = 'create-post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'update-post'), #! Automatically uses create form and html !!!
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'delete-post'),
    path('user/<str:username>', views.UserPostListView.as_view(template_name ='blog/user_posts.html'), name = 'user-posts'),

]
