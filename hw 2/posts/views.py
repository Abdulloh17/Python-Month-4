from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def time(request):
    time = datetime.now()
    return HttpResponse(time)


def goodbye(request):
    body = '''
    <h1>GoodBye!</h1>
    '''
    return HttpResponse(body)
