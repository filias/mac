from django.shortcuts import render

from mac.common import common
from mac.publicacoes.models import Link

RTR_DICT = common.DEFAULT_DICT


def resultados(request):
    return render(request, "templates/resultados.html", RTR_DICT)


def arte(request):
    return render(request, "templates/arte.html", RTR_DICT)


def servicos(request):
    return render(request, "templates/servicos.html", RTR_DICT)


def mapa(request):
    return render(request, "templates/mapa.html", RTR_DICT)


def links(request):
    RTR_DICT["links_list"] = Link.objects.all()
    return render(request, "templates/links.html", RTR_DICT)
