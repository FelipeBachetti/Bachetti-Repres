from django.shortcuts import render
from django.http import HttpResponse
from .models import Empresa, Tipo_Produto, Produto

def home(request):
    return render(request, 'home.html')

def company_page(request):
    return render(request, 'company_page.html')
