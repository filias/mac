from django.contrib import admin

from mac.gallery.models import (
    Anniversary,
    Award,
    Awardee,
    Exhibition,
    Foto,
    Gallery,
    Link,
    Publication,
    Snippet,
    Text,
)


class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "exhibition_type")
    ordering = ["-start_date"]
    fieldsets = [
        (
            "Geral",
            {
                "fields": [
                    "title",
                    "exhibition_type",
                    "art_type",
                    "start_date",
                    "end_date",
                    "galleries",
                ]
            },
        ),
        (
            "Detalhes",
            {"fields": ["description", "description_en", "artists", "art_works"]},
        ),
        (
            "Ficheiros",
            {"fields": ["catalog", "invitation", "press_release", "canvases", "fotos"]},
        ),
    ]
    list_filter = ["start_date", "art_type", "galleries", "artists"]
    date_hierarchy = "start_date"

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_type", "date", "artist", "author", "editor")
    ordering = ["title"]
    fieldsets = [
        (
            "Geral",
            {
                "fields": [
                    "title",
                    "author",
                    "editor",
                    "publication_type",
                    "date",
                    "artist",
                ]
            },
        ),
        ("Detalhes", {"fields": ["description", "description_en"]}),
        ("Ficheiros", {"fields": ["file"]}),
    ]
    list_filter = ["publication_type", "date", "artist", "author", "editor"]


class TextAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "text_en")
    ordering = ["title"]


class LinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    ordering = ["name"]
    fields = ["name", "url"]


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name", "street", "city")
    ordering = ["name"]
    fieldsets = [
        ("Geral", {"fields": ["name", "description"]}),
        ("Morada", {"fields": ["street", "zip_code", "city", "map"]}),
        ("Contactos", {"fields": ["phone", "email", "opening_times"]}),
        ("Fotos", {"fields": ["fotos"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


class AwardeeAdmin(admin.ModelAdmin):
    list_display = ("name", "profession")
    ordering = ["name"]
    fieldsets = [
        ("Geral", {"fields": ["name", "profession"]}),
        ("Foto", {"fields": ["foto"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


class AnniversaryAdmin(admin.ModelAdmin):
    list_display = ("date", "description")
    ordering = ["date"]
    fieldsets = [
        ("Geral", {"fields": ["date", "description", "trophy"]}),
        ("Detalhes", {"fields": ["invitation", "catalog"]}),
        ("Fotos", {"fields": ["fotos"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


class AwardAdmin(admin.ModelAdmin):
    list_display = ("anniversary", "name", "awardee", "description")
    ordering = ["name"]
    fieldsets = [
        ("Geral", {"fields": ["anniversary", "name", "awardee"]}),
        ("Detalhes", {"fields": ["description"]}),
        ("Foto", {"fields": ["foto"]}),
    ]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


class FotoAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "thumbnail")
    ordering = ["name"]
    search_fields = ["name", "image"]

    class Media:
        js = ["/media/filebrowser/js/AddFileBrowser.js"]


class SnippetAdmin(admin.ModelAdmin):
    list_display = ("name", "is_visible", "image", "text", "ordering", "url")
    ordering = ["is_visible", "name"]
    list_filter = ["is_visible", "name", "ordering"]


# Register admin models
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Awardee, AwardeeAdmin)
admin.site.register(Anniversary, AnniversaryAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Snippet, SnippetAdmin)
