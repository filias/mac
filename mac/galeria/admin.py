from django.db import models
from django.contrib import admin
from mac.galeria.models import Galeria, Staff, Premiado, Aniversario, Premio


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "rua", "cidade")
    ordering = ["nome"]
    fieldsets = [
        ("Geral", {"fields": ["nome", "descricao"]}),
        ("Morada", {"fields": ["rua", "cod_postal", "cidade", "mapa"]}),
        ("Contactos", {"fields": ["telefone", "email", "horario"]}),
        ("Fotos", {"fields": ["fotos"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


admin.site.register(Galeria, GaleriaAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ("nome", "funcao", "email")
    ordering = ["nome"]
    fieldsets = [
        ("Geral", {"fields": ["nome", "funcao"]}),
        ("Contactos", {"fields": ["telefone", "email"]}),
        ("Foto", {"fields": ["foto"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


admin.site.register(Staff, StaffAdmin)


class PremiadoAdmin(admin.ModelAdmin):
    list_display = ("nome", "profissao")
    ordering = ["nome"]
    fieldsets = [
        ("Geral", {"fields": ["nome", "profissao"]}),
        ("Foto", {"fields": ["foto"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


admin.site.register(Premiado, PremiadoAdmin)


class AniversarioAdmin(admin.ModelAdmin):
    list_display = ("data", "descricao")
    ordering = ["data"]
    fieldsets = [
        ("Geral", {"fields": ["data", "descricao", "trofeu"]}),
        ("Detalhes", {"fields": ["convite", "catalogo"]}),
        ("Fotos", {"fields": ["fotos"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


admin.site.register(Aniversario, AniversarioAdmin)


class PremioAdmin(admin.ModelAdmin):
    list_display = ("aniversario", "nome", "premiado", "descricao")
    ordering = ["nome"]
    fieldsets = [
        ("Geral", {"fields": ["aniversario", "nome", "premiado"]}),
        ("Detalhes", {"fields": ["descricao"]}),
        ("Foto", {"fields": ["foto"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


admin.site.register(Premio, PremioAdmin)
