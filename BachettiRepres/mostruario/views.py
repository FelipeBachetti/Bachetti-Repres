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

def product_page(request, id_emp, id_tip):
    produtos = Produto.objects.filter(tipo_id=id_tip)
    context={
        'produtos': produtos
    }
    return render(request, 'product_page.html', context)
