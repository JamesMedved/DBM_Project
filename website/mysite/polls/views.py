from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')
    
def search(request):
    # Grab search input
    searched = request.POST['searched']
    # Search for title if input is not empty
    if request.method == "POST" and searched:
        title_set = Titles.objects.filter(name__icontains=searched)
        return render(request, 'search.html', {'title_set': title_set})
    else:
        return render(request, 'search.html', {})

