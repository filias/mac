from django.contrib import admin

from mac.artistas.models import Artista, Obra


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nome", "artista_mac")
    ordering = ["nome", "artista_mac"]
    fieldsets = [
        ("Geral", {"fields": ["nome", "artista_mac", "tipo"]}),
        ("Biografia", {"fields": ["bio_resumo", "bio_resumo_en", "biografia"]}),
        ("Imagens", {"fields": ["foto", "foto_obra", "telas"]}),
    ]


admin.site.register(Artista, ArtistaAdmin)


class ObraAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "tipo", "estado")
    ordering = ["titulo"]
    fieldsets = [
        ("Geral", {"fields": ["titulo", "ano", "tipo", "autor"]}),
        (
            "Detalhes",
            {
                "fields": [
                    "descricao",
                    "descricao_en",
                    "estado",
                    "tecnicas",
                    "materiais",
                    "altura",
                    "largura",
                    "profundidade",
                ]
            },
        ),
        ("Imagens", {"fields": ["foto"]}),
    ]
    list_filter = ["tipo", "ano", "autor", "estado"]


admin.site.register(Obra, ObraAdmin)
