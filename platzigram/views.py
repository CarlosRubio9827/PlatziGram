# PlatziGram Views
# Django Response
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json

def helloWorld(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello World {now}'.format(now=str(now)))


def sorted(request):
    numbers = json.dumps(sorted([int(number) for number in request.GET['numbers'].split(',')]))
    print(type(numbers))
    print(numbers)

    return JsonResponse({ "numbers" : numbers})

def sayHi(request, nombre, edad):
    
    if edad < 18 :
        mensaje = nombre,' no puede ingresar a la página, tiene ',edad,' años'
    else:
        mensaje = nombre,' sí puede ingresar a la página, tiene ',edad,' años'

    return HttpResponse(mensaje)