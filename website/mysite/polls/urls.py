# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('home/', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('admin/', admin.site.urls),
]