from django.db import models
from django.contrib import admin
from mac.exposicoes.models import Exposicao


class ExposicaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_inicio", "data_fim", "tipo")
    ordering = ["-data_inicio"]
    fieldsets = [
        (
            "Geral",
            {
                "fields": [
                    "titulo",
                    "tipo",
                    "tipo_arte",
                    "data_inicio",
                    "data_fim",
                    "galerias",
                ]
            },
        ),
        ("Detalhes", {"fields": ["descricao", "descricao_en", "artistas", "obras"]}),
        (
            "Ficheiros",
            {"fields": ["catalogo", "convite", "press_release", "telas", "fotos"]},
        ),
    ]
    list_filter = ["data_inicio", "tipo_arte", "galerias", "artistas"]
    date_hierarchy = "data_inicio"

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


admin.site.register(Exposicao, ExposicaoAdmin)
