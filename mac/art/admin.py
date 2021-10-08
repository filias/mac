from django.contrib import admin

from mac.art.models import Artist, ArtWork, ArtMaterial, ArtType, ArtTechnique, Canvas


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "mac_artist")
    ordering = ["name", "mac_artist"]
    fieldsets = [
        ("Geral", {"fields": ["name", "mac_artist", "art_type"]}),
        ("Biografia", {"fields": ["bio_short", "bio_short_en", "bio"]}),
        ("Imagens", {"fields": ["foto", "foto_art_work", "canvases"]}),
    ]


class ArtWorkAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year", "art_work_type", "state")
    ordering = ["title"]
    fieldsets = [
        ("Geral", {"fields": ["title", "year", "art_work_type", "author"]}),
        (
            "Detalhes",
            {
                "fields": [
                    "description",
                    "description_en",
                    "state",
                    "techniques",
                    "materials",
                    "height",
                    "width",
                    "depth",
                ]
            },
        ),
        ("Imagens", {"fields": ["foto"]}),
    ]
    list_filter = ["art_work_type", "year", "author", "state"]


class CanvasAdmin(admin.ModelAdmin):
    list_display = ("title", "image")
    ordering = ["title"]


class ArtTechniqueAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    ordering = ["name"]
    list_filter = ["category"]


class ArtMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    ordering = ["name"]
    list_filter = ["category"]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtWork, ArtWorkAdmin)
admin.site.register(ArtType)
admin.site.register(Canvas, CanvasAdmin)
admin.site.register(ArtTechnique, ArtTechniqueAdmin)
admin.site.register(ArtMaterial, ArtMaterialAdmin)
