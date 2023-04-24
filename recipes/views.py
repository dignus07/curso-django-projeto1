# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Magnanumus Decimus Meridium'
    })


def sobre(request):
    return render(request, 'tempe-me/sobre.html')


def contato(request):
    return render(request, 'recipes/contato.html')
