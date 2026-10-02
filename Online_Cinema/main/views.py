from django.shortcuts import render, redirect
from .data import movies, genres, translations

def index(request):

    if request.method=='POST':

        theme=request.POST.get('theme','light')
        lang=request.POST.get('lang','ru')
        genre=request.POST.get('genre','all')
        response=redirect('index')
        if 'theme' in request.POST:
            response.set_cookie('theme',theme,max_age=60*60*24*365)
        if 'lang' in request.POST:
            response.set_cookie('lang',lang,max_age=60*60*24*365)
        if 'genre' in request.POST:
            response.set_cookie('sort_genre',genre,max_age=60*60*24*365)

        return response

    elif request.method=="GET":
        theme=request.COOKIES.get('theme','light')
        lang=request.COOKIES.get('lang','ru')
        sort_genre=request.COOKIES.get('sort_genre','all')

        movies_tr=movies.get(lang,movies['ru'])
        genres_tr=genres.get(lang,genres['ru'])
        transl=translations.get(lang, translations['ru'])
        context={
        'genres':genres_tr,
        'theme':theme,
        'lang':lang,
        'sort_genre':sort_genre,
        'transl':transl,
        'movies':movies_tr
    }
        return render(request,'main/index.html',context)
