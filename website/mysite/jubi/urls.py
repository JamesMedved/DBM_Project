# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('watchlater/', views.watch_later, name='watchlater'),
    path('watched/', views.watched, name='watched'),
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('home/', views.home, name='home'),
    path('udw', views.update_watched, name='udw'),
]