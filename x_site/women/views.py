from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

def index(request):
    posts = Women.objects.all()
    cat = Category.objects.all()
    arg = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat': cat}
    return render(request, 'women/index.html', context=arg)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def add_page(req):
    return HttpResponse('some')

def contact(req):
    return HttpResponse('some')

def login(req):
    return HttpResponse('some')

def show_post(req, post_id):
    girl_info = Women.objects.filter(id=post_id)
    return HttpResponse(f'{girl_info[0].content}')

def category(request, cat_id):
    posts = Women.objects.filter(category_id=cat_id)
    cat = Category.objects.all()
    arg = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat': cat}
    return render(request, 'women/index.html', context=arg)
