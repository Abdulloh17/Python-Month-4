from django.shortcuts import render

def index(request):
    context = {
        "title": "Главная страница",
        "my_list": [1, 2, 3, 4]
    }
    return render(request, "index.html", context=context)


def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")