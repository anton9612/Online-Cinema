from django.shortcuts import render
from .data import movies, genres

def index(request):
    context={
        'movies':movies,
        'genres':genres,
    }
    return render(request,'main/index.html',context)
