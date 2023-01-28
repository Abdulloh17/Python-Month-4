from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.shortcuts import render

from posts.models import Post

# передача строк в ответ
def hello(request):
    return HttpResponse("GeekTech")

def index(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "my_list": [1, 2, 3, 4, 5],
        "posts": posts
    }
    return render(request, "index.html", context)

def get_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Такого поста нет!")
    return render(request, "post_detail.html", {"post": post})

def about(request):
    context = {
        "title": "О нас",
    }
    return render(request, "about.html", context)
def contacts(request):
    context = {
        "title": "Контакты",
    }
    return render(request, "contacts.html", context)