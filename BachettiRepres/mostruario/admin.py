from django.contrib import admin

from .models import(
    Empresa, Tipo_Produto, Produto
)

@admin.register(Empresa)
class EmpresaModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

@admin.register(Tipo_Produto)
class Tipo_ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'empresa']

@admin.register(Produto)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'tipo']
