from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def getRandom():
    return random.randint(1, 10)


def index(request):
    title = 'my blog'
    mylist = [10, 20, 30]
    mydict = {'Student1': 'Ilon', 'Student2': 'Ben'}
    mytuple = (1, 2, 3, 4, 5)
    data = {'title': title, 'mylist': mylist, 'mydict': mydict, 'mytuple': mytuple, 'randNum': getRandom}
    return render(request, 'testapp/index.html', data)


def form(request):
    return render(request, 'testapp/form.html')


def save(request):
    title = request.POST.get('title')
    description = request.POST.get('description')

    return render(request, 'testapp/save.html', {'title': title, 'description': description})















