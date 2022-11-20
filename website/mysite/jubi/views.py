from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import F
from .models import Titles, Streaming, WatchLater, Watched
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from datetime import date
from collections import Counter
from itertools import chain

# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    # Search for title if input is not empty
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Streaming.objects.filter(title__name__icontains=search), 'search':search})

    # Get watched and watch later titles
    qset = list(chain(WatchLater.objects.filter(user_id=request.user.id), Watched.objects.filter(user_id=request.user.id)))
    return render(request, 'home.html', 
    {
        'aset': get_actor_recs(qset),
        'sset': get_sequel_recs(qset)
    })

@login_required(login_url='loginPage')
def title(request):
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Streaming.objects.filter(title__name__icontains=search), 'search':search})

        # Return title information
        title = request.POST.get('title')
        if title:
            title_set = Streaming.objects.filter(title_id=title)
            return render(request, 'title.html', {'tset': title_set, 'title': title_set[0]})

@login_required(login_url='loginPage')
def search(request):
    # Search for title if input is not empty
    if request.method == "POST":
        search = request.POST.get('search')
        wl_id = request.POST.get('add_wl')
        w_id = request.POST.get('add_w')

        # Check for new search
        if search:
            return render(request, 'search.html', {'tset': Streaming.objects.filter(title__name__icontains=search), 'search':search})

        # Insert into watch later table
        if wl_id:
            WatchLater(title_id=wl_id, user_id=request.user.id, date_added=date.today()).save()

        # Insert into watched table
        if w_id:
            Watched(title_id = w_id, user_id=request.user.id).save()

    # Get watched and watch later titles
    qset = list(chain(WatchLater.objects.filter(user_id=request.user.id), Watched.objects.filter(user_id=request.user.id)))
    return render(request, 'home.html', 
    {
        'aset': get_actor_recs(qset),
        'dset': get_director_recs(qset),
        'sset': get_sequel_recs(qset)
    })

@login_required(login_url='loginPage')
def watch_later(request):
    # title_set = Titles.objects.filter(id=watch_later_set)
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Streaming.objects.filter(title__name__icontains=search), 'search':search})

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
            
    return render(request, 'watch_later.html', {'tset': WatchLater.objects.filter(user_id=request.user.id).order_by(F('priority').desc(nulls_last=True))})

@login_required(login_url='loginPage')
def watched(request):
    # title_set = Titles.objects.filter(id=watch_later_set)
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Streaming.objects.filter(title__name__icontains=search), 'search':search})

        # Delete from watch later table
        del_id = request.POST.get('btn_del')
        if del_id:
            Watched.objects.get(title_id=del_id, user_id=request.user.id).delete()
        
        # Update priority of watch later record
        new_rat = request.POST.get('dp_rat')
        w_id = request.POST.get('w_id')
        if new_rat:
            w_obj = Watched.objects.get(title_id=w_id, user_id=request.user.id)
            w_obj.rating = new_rat
            w_obj.save()
            
    return render(request, 'watched.html', {'tset': Watched.objects.filter(user_id=request.user.id).order_by(F('rating').desc(nulls_last=True))})

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

def get_actor_recs(qset):
    actors = []
    for title in qset:
        if title.title.cast:
            actors_lst = title.title.cast.split(',')
            for i in range(len(actors_lst)):
                actors.append(actors_lst[i]) 
    actors = [key for key, value in Counter(actors).most_common()][:5]
    actor_titles = [Titles.objects.filter(cast__icontains=actor) for actor in actors]
    return zip(actors, actor_titles)

def get_sequel_recs(qset):
    titles = []
    similar_titles = []
    for title in qset:
        base_name = title.title.name
        if ':' in base_name:
            base_name = base_name.split(':')[0]
        if title.title.name not in titles:
            titles.append(title.title.name)
            similar_titles.append(Titles.objects.filter(name__icontains=base_name).exclude(name=title.title.name))
    return zip(titles, similar_titles)

def get_director_recs(qset):
    directors = []
    for title in qset:
        if title.title.director:
            directors.append(title.title.director.split(',')[0]) 
    directors = [key for key, value in Counter(directors).most_common()][:5]
    director_titles = [Titles.objects.filter(director__icontains=director) for director in directors]
    return zip(directors, director_titles)