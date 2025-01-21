from django.shortcuts import render
from django.http import HttpResponse
from .models import Empresa, Tipo_Produto, Produto

def home(request):
    empresas = Empresa.objects.all().values()
    context = {
        'empresas': empresas,
    }
    return render(request, 'home.html', context)



