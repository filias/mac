# -*- coding: utf-8 -*
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mac.galeria.models import Galeria
from mac.artistas.models import Artista, Obra
from mac.geral.models import Tipo, Foto, Tela
from mac.publicacoes.models import Publicacao

TIPO_CHOICES = (
	(u'I', u'Individual'), 
	(u'C', u'Colectiva'),
)

# Create your models here.
class Exposicao(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=True)
    tipo_arte = models.ManyToManyField(Tipo)
    descricao = models.TextField(null=True, blank=True)
    descricao_en = models.TextField(null=True, blank=True)
    data_inicio = models.DateField(u'data de inicio')
    data_fim = models.DateField(u'data de fim')
    galerias = models.ManyToManyField(Galeria)
    artistas = models.ManyToManyField(Artista, blank=True)
    obras = models.ManyToManyField(Obra, blank=True)
    fotos = models.ManyToManyField(Foto, blank=True)
    catalogo = models.ForeignKey(Publicacao, null=True, blank=True, limit_choices_to = {'tipo__exact': "Catalogo"})
    convite = models.FileField(upload_to='convites/', null=True, blank=True)
    press_release = models.FileField(upload_to='press_releases/', null=True, blank=True)
    telas = models.ManyToManyField(Tela)
    
    def __str__(self):
        return self.titulo

    def exposicao_actual(self):
        return (self.data_inicio <= datetime.date.today() and self.data_fim >= datetime.date.today())

    def exposicao_passada(self):
        return self.data_fim < datetime.date.today()

    def exposicao_futura(self):
        return self.data_inicio > datetime.date.today()

    class Meta:
        ordering = ['-data_inicio']
        verbose_name = _('Exposicao')
        verbose_name_plural = _('Exposicoes')
