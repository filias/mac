from django.db import models
from django.contrib import admin
from mac.publicacoes.models import Publicacao, Texto, Link

class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data', 'artista', 'autor', 'editor')
    ordering = ['titulo']
    fieldsets = [
        ('Geral', {'fields': ['titulo', 'autor', 'editor','tipo', 'data', 'artista']}),
        ('Detalhes', {'fields': ['descricao', 'descricao_en']}),
        ('Ficheiros', {'fields': ['ficheiro']}),
    ]
    list_filter = ['tipo', 'data', 'artista', 'autor', 'editor']
        
admin.site.register(Publicacao, PublicacaoAdmin)

class TextoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'texto_en')
    ordering = ['titulo']

admin.site.register(Texto, TextoAdmin)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('nome', 'url')
    ordering = ['nome']
    fields = ['nome', 'url']

admin.site.register(Link, LinkAdmin)
