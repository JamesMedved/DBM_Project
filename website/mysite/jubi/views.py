from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import F
from .models import Titles, Streaming, WatchLater, Watched, Friends
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from datetime import date
from collections import Counter
from itertools import chain
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    # Search for title if input is not empty
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search)), 'search':search})

    # Get watched and watch later titles
    qset = list(chain(WatchLater.objects.filter(user_id=request.user.id), Watched.objects.filter(user_id=request.user.id)))
    return render(request, 'home.html', {'aset': get_actor_recs(qset), 'dset': get_director_recs(qset), 'sset': get_similar_recs(qset)})

@login_required(login_url='loginPage')
def social(request):
    # Search for title if input is not empty
    if request.method == "POST":
        # Check for new search
        title_search = request.POST.get('search')
        if title_search:
            return render(request, 'search.html', {'tset': Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search)), 'search':search})

        # Check for user search
        user_search = request.POST.get('friend_search')
        if user_search:
            return render(request, 'social.html', 
            {'fset': Friends.objects.filter(user_id=request.user.id),
            'uset': User.objects.filter(username=user_search).exclude(id=request.user.id), 
            'search':user_search})

        # Insert into watch later table
        add_friend = request.POST.get('add_fr')
        if add_friend:
            Friends.objects.update_or_create(user_id=request.user.id, friend_id=add_friend)

        # Delete from watch later table
        del_id = request.POST.get('btn_del')
        if del_id:
            Friends.objects.get(user_id=request.user.id, friend_id=del_id).delete()
    
    return render(request, 'social.html', {'fset': Friends.objects.filter(user_id=request.user.id)})

@login_required(login_url='loginPage')
def friend(request):
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search)), 'search':search})

        # Return title information
        friend_id = request.POST.get('friend')
        if title:
            return render(request, 'friend.html', 
            {'friend': User.objects.filter(id=friend_id)[0],
            'wlset': WatchLater.objects.filter(user_id=friend_id).order_by(F('priority').desc(nulls_last=True)),
            'wset': Watched.objects.filter(user_id=friend_id).order_by(F('rating').desc(nulls_last=True))})

@login_required(login_url='loginPage')
def title(request):
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search)), 'search':search})

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
            return render(request, 'search.html', {'tset': Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search)), 'search':search})

        # Insert into watch later table
        if wl_id:
            WatchLater(title_id=wl_id, user_id=request.user.id, date_added=date.today()).save()

        # Insert into watched table
        if w_id:
            Watched(title_id = w_id, user_id=request.user.id, finished=date.today()).save()
        
    # Get watched and watch later titles
    qset = list(chain(WatchLater.objects.filter(user_id=request.user.id), Watched.objects.filter(user_id=request.user.id)))
    return render(request, 'home.html', {'aset': get_actor_recs(qset), 'dset': get_director_recs(qset), 'sset': get_similar_recs(qset)})

@login_required(login_url='loginPage')
def watch_later(request):
    # title_set = Titles.objects.filter(id=watch_later_set)
    if request.method == "POST":
        # Check for new search
        search = request.POST.get('search')
        if search:
            return render(request, 'search.html', {'tset': Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search)), 'search':search})

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
            return render(request, 'search.html', {'tset': Titles.objects.filter(Q(name__icontains=search) | Q(cast__icontains=search) | Q(director__icontains=search)), 'search':search})

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
        return redirect('home')
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
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def get_actor_recs(qset):
    actors = []
    actor_titles = []
    # Get cast for each title in watched and watch later tables
    for title in qset:
        if title.title.cast:
            actors_lst = title.title.cast.split(',')
            for i in range(len(actors_lst)):
                actors.append(actors_lst[i]) 
    # Get top 5 actors from watched and watch later tables
    actors = [key for key, value in Counter(actors).most_common()][:5]
    # Get titles for each of top 5 actors as long as more than two are returned
    for actor in actors:
        query = Titles.objects.filter(cast__icontains=actor)
        if len(query) > 3:
            actor_titles.append(query)
        else:
            actors.remove(actor)
    return zip(actors, actor_titles)

def get_similar_recs(qset):
    titles = []
    similar_titles = []
    # Get similar titles for each title in watched and watch later tables
    for title in qset:
        # Get get base name
        base_name = title.title.name
        if ':' in base_name:
            base_name = base_name.split(':')[0]
        if base_name[-1].isdigit():
            base_name = base_name[:-1]
        # Make sure not to display the move the similar recommendations are based on
        # Get similar titles as long as more than two are returned
        if title.title.name not in titles:
            query = Titles.objects.filter(name__icontains=base_name).exclude(name=title.title.name)
            if len(query) > 3:
                titles.append(title.title.name)
                similar_titles.append(query)
    return zip(titles, similar_titles)

def get_director_recs(qset):
    directors = []
    director_titles = []
    # Get director for each title in watched and watch later tables
    for title in qset:
        if title.title.director:
            directors.append(title.title.director.split(',')[0]) 
    # Get top 5 directors from watched and watch later tables
    directors = [key for key, value in Counter(directors).most_common()][:5]
    # Get titles for each of top 5 directors as long as more than two are returned
    for director in directors:
        query = Titles.objects.filter(director__icontains=director)
        if len(query) > 3:
            director_titles.append(query)
        else:
            directors.remove(director)
    return zip(directors, director_titles)