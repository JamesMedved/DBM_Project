from django.http import HttpResponse
from django.shortcuts import render
from .models import Titles

# Create your views here.
def search(request):
    # Grab search input
    search = request.POST.get('search', '')
    # Search for title if input is not empty
    if request.method == "POST" and search:
        title_set = Titles.objects.filter(name__icontains=search)
        return render(request, 'search.html', {'title_set': title_set, 'search':search})
    else:
        return render(request, 'search.html', {})

