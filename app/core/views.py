from django.http.response import HttpResponse
from django.shortcuts import render
from  django.http import HttpResponse, JsonResponse

from core.models import Category, Product

# Create your views here.
def myFirstView(request):
    #return HttpResponse('Hola, esta es mi primera URL')
    data = {
        'name': 'Antonio',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)

def mySecondView(request):
    data = {
        'name': 'Antonio',
        'products': Product.objects.all()
    }
    return render(request, 'secont.html', data)
