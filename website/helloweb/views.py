from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from app')

def django(request):
    return HttpResponse('Hello from django')

def about(request):
    return HttpResponse('<h3>Hello, I am human<h3>')



