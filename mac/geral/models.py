from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField


class Tela(models.Model):
    titulo = models.CharField(max_length=200)
    image = models.ImageField(upload_to='geral/')
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']

class Tipo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']


class Tecnica(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = _('Tecnica')
        verbose_name_plural = _('Tecnicas')

class Material(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = _('Material')
        verbose_name_plural = _('Materiais')
        
class Foto(models.Model):
    nome = models.CharField(max_length=100)
    thumbnail = FileBrowseField(max_length=200, directory="/", extensions=['.jpg', '.jpeg', '.gif','.png','.tif','.tiff'], blank=True, null=True)
    image = FileBrowseField(max_length=200, directory="/", extensions=['.jpg', '.jpeg', '.gif','.png','.tif','.tiff'], blank=True, null=True)
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
        

class Destaque(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='inicial/', null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    texto_en = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=100)
    visivel = models.BooleanField(default=False)
    ordem = models.SmallIntegerField()
    
    def __str__(self):
        return self.url
    
    class Meta:
        ordering = ['nome']
    
