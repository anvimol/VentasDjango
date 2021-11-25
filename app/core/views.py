from django.http.response import HttpResponse
from django.shortcuts import render
from  django.http import HttpResponse, JsonResponse

# Create your views here.
def myFirstView(request):
    #return HttpResponse('Hola, esta es mi primera URL')
    data = {
        'name': 'Antonio'
    }
    return render(request, 'index.html', data)
