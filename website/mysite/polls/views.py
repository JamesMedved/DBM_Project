from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Titles
from .models import WatchLater
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def search(request):
    search = request.POST.get('search')
    # Search for title if input is not empty
    if request.method == "POST":
        if search:
            title_set = Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search))
            return render(request, 'search.html', {'title_set': title_set, 'search':search})
        # Insert into watch later table
        add_wl = WatchLater(title_id=request.POST.get('add_wl'), user_id=1)
        add_wl.save()
    return render(request, 'search.html', {})

def watch_later(request):
    title_set = WatchLater.objects.all()
    return render(request, 'watch_later.html', {'title_set': title_set})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'register.html', context)

def login(request):
    return render(request,'login.html')