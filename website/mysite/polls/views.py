from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Titles
from .models import WatchLater


# Create your views here.
def search(request):
    # Grab search input
    search = request.POST.get('search', '')
    # Search for title if input is not empty
    if request.method == "POST" and search:
        title_set = Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search))
        return render(request, 'search.html', {'title_set': title_set, 'search':search})
    else:
        return render(request, 'search.html', {})

def watch_later(request):
    title_set = WatchLater.objects.all()
    return render(request, 'watch_later.html', {'title_set': title_set})