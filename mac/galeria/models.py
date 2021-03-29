from django.db import models
from django.contrib import admin
from mac.geral.models import Foto
from mac.artistas.models import Obra
import datetime

# Create your models here.
class Galeria(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    rua = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=30, null=True, blank=True)
    cod_postal = models.CharField(max_length=8, null=True, blank=True)
    telefone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(max_length=75, null=True, blank=True)
    horario = models.CharField(max_length=200, null=True, blank=True)
    fotos = models.ManyToManyField(Foto, blank=True)
    mapa = models.URLField(null=True, blank=True)
    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        
class Staff(models.Model):
    nome = models.CharField(max_length=150)
    funcao = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=75, null=True, blank=True)
    telefone = models.CharField(max_length=13, null=True, blank=True)
    foto = models.ForeignKey(Foto, null=True, blank=True)
    def __unicode__(self):
        return self.nome
        
    class Meta:
        ordering = ['nome']

class Premiado(models.Model):
    nome = models.CharField(max_length=150)
    profissao = models.CharField(max_length=50, null=True, blank=True)
    foto = models.ForeignKey(Foto, null=True, blank=True)
    def __unicode__(self):
        return self.nome
        
    class Meta:
        ordering = ['nome']

class Aniversario(models.Model):
    data = models.DateField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    trofeu = models.ForeignKey(Obra, null=True, blank=True)
    convite = models.FileField(upload_to='convites/', null=True, blank=True)
    catalogo = models.FileField(upload_to='catalogos/', null=True, blank=True)
    fotos = models.ManyToManyField(Foto, blank=True)
    def __unicode__(self):
        return self.descricao
        
    class Meta:
        ordering = ['data']

class Premio(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    premiado = models.ForeignKey(Premiado, null=True, blank=True)
    aniversario = models.ForeignKey(Aniversario, null=True, blank=True)
    foto = models.ForeignKey(Foto, null=True, blank=True)
    def __unicode__(self):
        return self.nome
        
    class Meta:
        ordering = ['nome']

