from mac.gallery.models import Gallery
from mac.art.models import Canvas


def contacts_renderer(request):
    gallery_list = Gallery.objects.filter(nome__startswith="MAC").order_by("-nome")
    return {"gallery_list": gallery_list}


def telas_renderer(request):
    telas = Canvas.objects.all()
    return {"telas": telas}
