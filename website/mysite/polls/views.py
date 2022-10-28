from django.http import HttpResponse
from django.shortcuts import render
from .models import Titles

# Create your views here.
def homepage(request):
    title_list = Titles.objects.all()
    return render(request, 'homepage.html', {'title_list': title_list})