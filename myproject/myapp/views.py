from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Тони старк умрёт в "Мстителях: ФИНАЛ".</h1>')