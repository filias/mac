from mac.art.models import Canvas
from mac.gallery.models import Gallery


def contacts_renderer(request):
    gallery_list = Gallery.objects.filter(name__startswith="MAC").order_by("-name")
    return {"gallery_list": gallery_list}


def telas_renderer(request):
    telas = Canvas.objects.all()
    return {"telas": telas}
