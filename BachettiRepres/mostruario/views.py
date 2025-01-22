from django.shortcuts import render
from django.http import HttpResponse
from .models import Empresa, Tipo_Produto, Produto

def home(request):
    return render(request, 'home.html')

def company_page(request, id):
    tipos = Tipo_Produto.objects.filter(empresa_id=id)
    context={
        'tipos': tipos,
    }
    return render(request, 'company_page.html', context)
