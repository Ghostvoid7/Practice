from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def monday(request):
    return HttpResponse('''<h1>Погода будет супер! +20 Зонтик не бери!</h1>
    <ul>
     <li> <a href="http://127.0.0.1:8000/weather/tuesday/">tuesday</a> </li>
     <li> <a href="http://127.0.0.1:8000/weather/wednesday/">wednesday</a> </li>
    </ul>
    ''' + f'<h3>{datetime.date.today()} </h3>')

def tuesday(request):
    return HttpResponse('''<h1>Погода будет супер! +30 Будет жарко!<h1> 
    <ul>
     <li> <a href="http://127.0.0.1:8000/weather/wednesday/"> <h6>wednesday</h6></a> </li>
     <li> <a href="http://127.0.0.1:8000/weather/thursday/"> <h6>thursday</h6></a> </li>
    </ul>
    ''')

def wednesday(request):
    return HttpResponse('<h1>Погода будет не очень! +10 Сиди дома!<h1>')

def thursday(request):
    return HttpResponse(f'{datetime.date.today()}')