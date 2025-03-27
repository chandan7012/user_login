from django.urls import path
from . import views

urlpatterns = [
    path('refresh', views.refresh_token),
    path('register', views.register),
    path('login', views.login),
]
