from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    link_imagem = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Tipo_Produto(models.Model):
    nome = models.CharField(max_length=80)
    empresa = models.ForeignKey('Empresa',on_delete=models.CASCADE,)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.ForeignKey('Tipo_Produto',on_delete=models.CASCADE,)
    link_imagem = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome
