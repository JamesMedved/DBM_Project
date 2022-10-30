from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Titles
from .models import WatchLater


# Create your views here.
def search(request):
    search = request.POST.get('search')
    # Search for title if input is not empty
    if request.method == "POST":
        if search:
            title_set = Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search))
            return render(request, 'search.html', {'title_set': title_set, 'search':search})
    return render(request, 'search.html', {})

def add_watch_later(request):
    add_wl_title_id = request.POST.get('add_wl')
    # Search for title if input is not empty
    if request.method == "POST":
        if add_wl_title_id:
            # wl = WatchLater(title_id=1, user_id=1)
            # wl.save()
            return render(request, 'search.html', {'wl':add_wl_title_id})

def watch_later(request):
    title_set = WatchLater.objects.all()
    return render(request, 'watch_later.html', {'title_set': title_set})