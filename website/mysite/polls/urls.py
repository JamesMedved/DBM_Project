# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('search', views.search, name='search'),
]