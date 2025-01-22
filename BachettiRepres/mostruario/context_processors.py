from .models import Empresa

def empresas_context(request):
    empresas = Empresa.objects.all().values()  # Consulta as empresas
    return {'empresas': empresas}