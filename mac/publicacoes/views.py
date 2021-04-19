from django.shortcuts import render

from mac.common import common
from mac.publicacoes.models import Publicacao

RTR_DICT = common.DEFAULT_DICT


def index(request):

    RTR_DICT["catalogos"] = Publicacao.objects.filter(tipo="Catalogo").order_by(
        "-data"
    )[:3]
    RTR_DICT["imprensa"] = Publicacao.objects.filter(tipo="Imprensa").order_by("-data")[
        :3
    ]
    RTR_DICT["criticas"] = Publicacao.objects.filter(tipo="Critica").order_by("-data")[
        :3
    ]
    return render(request, "publicacoes.html", RTR_DICT)


def catalogos(request, select):
    RTR_DICT["publicacoes"] = Publicacao.objects.filter(
        tipo="Catalogo", artista__nome__range=(select[0], select[1])
    ).order_by("artista")
    return render(request, "publicacoes_catalogos.html", RTR_DICT)


def imprensa(request, select):
    RTR_DICT["publicacoes"] = Publicacao.objects.filter(
        tipo="Imprensa", artista__nome__range=(select[0], select[1])
    ).order_by("artista")
    return render(request, "publicacoes_imprensa.html", RTR_DICT)


def critica(request, select):
    RTR_DICT["publicacoes"] = Publicacao.objects.filter(
        tipo="Critica", artista__nome__range=(select[0], select[1])
    ).order_by("artista")
    return render(request, "publicacoes_criticas.html", RTR_DICT)
