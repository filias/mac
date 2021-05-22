from __future__ import absolute_import

from django.contrib import admin
from django.utils.html import format_html
from filebrowser.settings import ADMIN_THUMBNAIL

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
    list_display = ("nome", "image_thumbnail")
    ordering = ["nome"]
    search_fields = ["nome", "image"]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]

    def image_thumbnail(self, obj):
        if obj.image and obj.image.filetype == "Image":
            return format_html('<img src="%s" />' % obj.thumbnail.url)
        else:
            return ""

    image_thumbnail.short_description = "Thumbnail"


admin.site.register(Foto, FotoAdmin)


class DestaqueAdmin(admin.ModelAdmin):
    list_display = ("nome", "visivel", "imagem", "texto", "ordem", "url")
    ordering = ["visivel", "nome"]
    list_filter = ["visivel", "nome", "ordem"]


admin.site.register(Destaque, DestaqueAdmin)
