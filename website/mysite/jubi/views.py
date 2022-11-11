from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Titles, Streaming, WatchLater, Watched
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from datetime import date

# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    search = request.POST.get('search')
    # Search for title if input is not empty
    if request.method == "POST":
        if search:
            title_set = Streaming.objects.filter(Q(title__icontains=search))
            return render(request, 'search.html', {'title_set': title_set, 'search':search})
    return render(request, 'home.html', {})

@login_required(login_url='loginPage')
def search(request):
    search = request.POST.get('search')
    # Search for title if input is not empty
    if request.method == "POST":
        if search:
            title_set = Streaming.objects.filter(Q(name__icontains=search))
            return render(request, 'search.html', {'title_set': title_set, 'search':search})
        # Insert into watch later table
        wl_id = request.POST.get('add_wl')
        w_id = request.POST.get('add_w')
        if wl_id:
            add_wl = WatchLater(title_id=wl_id, user_id=request.user.id, date_added=date.today())
            add_wl.save()
        if w_id:
            add_w = Watched(title_id = w_id, user_id=request.user.id)
            add_w.save()
    return render(request, 'search.html', {})


# TODO: Fix so the page isn't reloaded every time
def update_watched(request):
    if request.method == "POST":
        # Insert into watch later table
        wl_id = request.POST.get('add_wl')
        w_id = request.POST.get('add_w')
        if wl_id:
            add_wl = WatchLater(title_id=wl_id, user_id=request.user.id, date_added=date.today())
            add_wl.save()
        if w_id:
            add_w = Watched(title_id = w_id, user_id=request.user.id)
            add_w.save()
        return render(request, 'home.html', {})

@login_required(login_url='loginPage')
def watch_later(request):
    # title_set = Titles.objects.filter(id=watch_later_set)
    if request.method == "POST":
        # Delete from watch later table
        del_id = request.POST.get('btn_del')
        if del_id:
            WatchLater.objects.get(title_id=del_id, user_id=request.user.id).delete()
        # Update priority of watch later record
        new_pri = request.POST.get('dp_pri')
        wl_id = request.POST.get('wl_id')
        if new_pri:
            wl_obj = WatchLater.objects.get(title_id=wl_id, user_id=request.user.id)
            wl_obj.priority = new_pri
            wl_obj.save()
            
    # TODO: Fix this later
    watch_later_set = WatchLater.objects.filter(user_id=request.user.id)
    title_set = Titles.objects.filter(id__in=watch_later_set.values_list("title_id"))
    comb_set = zip(watch_later_set, title_set)
    return render(request, 'watch_later.html', {'watch_later_set': watch_later_set,'comb_set': comb_set})

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

@login_required(login_url='loginPage')
def watched(request):
    # title_set = Titles.objects.filter(id=watch_later_set)
    if request.method == "POST":
        # Delete from watch later table
        del_id = request.POST.get('btn_del')
        if del_id:
            Watched.objects.get(title_id=del_id, user_id=request.user.id).delete()

    watched_set = Watched.objects.filter(user_id=request.user.id)
    title_set = Titles.objects.filter(id__in=watched_set.values_list("title_id"))
    comb_set = zip(watched_set, title_set)
    return render(request, 'watched.html', {'watched_set': watched_set,'comb_set': comb_set})
