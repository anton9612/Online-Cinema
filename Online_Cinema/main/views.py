from django.shortcuts import render, redirect
from .data import movies, genres, translations

def index(request):

    if request.method=='POST':
        theme=request.POST.get('theme','light')
        lang=request.POST.get('lang','ru')
        response=redirect('index')
        response.set_cookie('theme',theme,max_age=60*60*24*365)
        response.set_cookie('lang',lang,max_age=60*60*24*365)
        return response

    elif request.method=="GET":
        theme=request.COOKIES.get('theme','light')
        lang=request.COOKIES.get('lang','ru')

        movies_tr=movies.get(lang,movies['ru'])
        genres_tr=genres.get(lang,genres['ru'])
        transl=translations.get(lang, translations['ru'])
        context={
        'genres':genres_tr,
        'theme':theme,
        'lang':lang,
        'transl':transl,
        'movies':movies_tr
    }
        return render(request,'main/index.html',context)
