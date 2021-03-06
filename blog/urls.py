from django.urls import path
from django.views import generic
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
