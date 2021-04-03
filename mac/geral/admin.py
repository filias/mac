from __future__ import absolute_import

from django.contrib import admin

from mac.geral.models import Destaque, Foto, Material, Tecnica, Tela, Tipo

admin.site.register(Tipo)


class TelaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "image")
    ordering = ["titulo"]


admin.site.register(Tela, TelaAdmin)


class TecnicaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria")
    ordering = ["nome"]
    list_filter = ["categoria"]


admin.site.register(Tecnica, TecnicaAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria")
    ordering = ["nome"]
    list_filter = ["categoria"]


admin.site.register(Material, MaterialAdmin)


class FotoAdmin(admin.ModelAdmin):
    list_display = ("nome", "image", "thumbnail")
    ordering = ["nome"]
    search_fields = ["nome", "image"]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


admin.site.register(Foto, FotoAdmin)


class DestaqueAdmin(admin.ModelAdmin):
    list_display = ("nome", "visivel", "imagem", "texto", "ordem", "url")
    ordering = ["visivel", "nome"]
    list_filter = ["visivel", "nome", "ordem"]


admin.site.register(Destaque, DestaqueAdmin)
