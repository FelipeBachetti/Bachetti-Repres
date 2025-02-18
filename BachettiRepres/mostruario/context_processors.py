from .models import Empresa

def empresas_context(request):
    empresas = Empresa.objects.prefetch_related("tipo_produto_set").all()
    return {'empresas': empresas}