from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """домашняя сраница"""
    return HttpResponse('<html><title>Кайт-клуб \"Вверх\"</title></html>')
