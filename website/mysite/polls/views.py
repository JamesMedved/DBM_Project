from django.http import HttpResponse
from django.shortcuts import render
from .models import Titles

# Create your views here.
def search(request):
    # Grab search input
    searched = request.POST.get('search', '')
    # Search for title if input is not empty
    if request.method == "POST" and searched:
        return render(request, 'search.html', {'title_set': Titles.objects.filter(name__icontains=searched)})
    else:
        return render(request, 'search.html', {})

