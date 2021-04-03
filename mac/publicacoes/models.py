from django.db import models
from django.utils.translation import ugettext_lazy as _

from mac.artistas.models import Artista

TIPO_CHOICES = (
    (u"Newsletter", u"Newsletter"),
    (u"Catalogo", u"Catalogo"),
    (u"Monografia", u"Monografia"),
    (u"Imprensa", u"Imprensa"),
    (u"Critica", u"Critica"),
)

# Create your models here.
class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100, null=True, blank=True)
    editor = models.CharField(max_length=100, null=True, blank=True)
    artista = models.ForeignKey(
        Artista, null=True, blank=True, on_delete=models.CASCADE
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data = models.DateField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    descricao_en = models.TextField(null=True, blank=True)
    ficheiro = models.FileField(
        upload_to="publicacoes/", max_length=200, null=True, blank=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-data"]
        verbose_name = _("Publicacao")
        verbose_name_plural = _("Publicacoes")


class Texto(models.Model):
    titulo = models.CharField(max_length=500)
    texto = models.TextField(null=True, blank=True)
    texto_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["titulo"]


class Link(models.Model):
    nome = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
