from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('subscribe/', views.newsletter, name='subscribe'),
    path('send_newsletter/', views.send_newsletter, name='send_newsletter'),
]