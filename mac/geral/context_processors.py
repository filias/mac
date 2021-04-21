from mac.galeria.models import Galeria
from mac.geral.models import Tela


def contacts_renderer(request):
    gallery_list = Galeria.objects.filter(nome__startswith="MAC").order_by("-nome")
    return {"gallery_list": gallery_list}


def telas_renderer(request):
    telas = Tela.objects.all()
    return {"telas": telas}
