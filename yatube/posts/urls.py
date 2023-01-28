from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'posts_index'),
    path('group/<slug:slug>/', views.group_posts, name = 'posts_group'),
]
