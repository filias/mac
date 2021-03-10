import datetime

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mac.geral.models import Tipo, Tecnica, Material, Tela, Foto

ESTADO_CHOICES = (
	(u'A', u'Acervo'), 
	(u'E', u'Exposicao'),
	(u'C', u'Coleccao'),
)

# Create your models here.
class Artista(models.Model):
    nome = models.CharField(max_length=100)
    bio_resumo = models.TextField(null=True, blank=True)
    bio_resumo_en = models.TextField(null=True, blank=True)
    foto = models.ForeignKey(Foto, null=True, blank=True, related_name='foto')
    foto_obra = models.ForeignKey(Foto, null=True, blank=True, related_name='foto_obra')
    biografia = models.FileField(upload_to='biografias/', null=True, blank=True)
    tipo = models.ManyToManyField(Tipo)
    telas = models.ManyToManyField(Tela, null=True, blank=True)
    artista_mac = models.BooleanField()
    
    def __unicode__(self):
        return self.nome
    
    def tem_acervo(self):
        obras = Obra.objects.filter(autor=self, estado='A')
        return obras
    
    class Meta:
        ordering = ['nome']
	verbose_name = _('Artista')
        verbose_name_plural = _('Artistas')
        

class Obra(models.Model):
    autor = models.ForeignKey(Artista)
    titulo = models.CharField(max_length=100)
    ano = models.CharField(max_length=12)
    descricao = models.TextField(null=True, blank=True)
    descricao_en = models.TextField(null=True, blank=True)
    tipo = models.ForeignKey(Tipo)
    tecnicas = models.ManyToManyField(Tecnica, null=True, blank=True)
    altura = models.IntegerField(null=True, blank=True)
    largura = models.IntegerField(null=True, blank=True)
    profundidade = models.IntegerField(null=True, blank=True)
    materiais = models.ManyToManyField(Material, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)
    foto = models.ForeignKey(Foto, null=True, blank=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.autor.nome, self.titulo)

    class Meta:
        ordering = ['autor', '-ano']
	verbose_name = _('Obra')
        verbose_name_plural = _('Obras')
