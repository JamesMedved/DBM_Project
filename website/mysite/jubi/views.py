from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Titles
from .models import WatchLater
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.
@login_required(login_url='loginPage')
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

@login_required(login_url='loginPage')
def watch_later(request):
    # title_set = Titles.objects.filter(id=watch_later_set)
    if request.method == "POST":
        # Delete from watch later table
        WatchLater.objects.get(title_id=request.POST.get('del_wl')).delete()
    watch_later_set = WatchLater.objects.all()
    return render(request, 'watch_later.html', {'title_set': watch_later_set})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('search')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('loginPage')

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('search')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('search')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')
