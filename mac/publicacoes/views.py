from django.shortcuts import render

from mac.publicacoes.models import Publicacao


def catalogos(request, select):
    context = {}
    context["publicacoes"] = Publicacao.objects.filter(
        tipo="Catalogo", artista__nome__range=(select[0], select[1])
    ).order_by("artista")
    return render(request, "publicacoes_catalogos.html", context)


def imprensa(request, select):
    context = {}
    context["publicacoes"] = Publicacao.objects.filter(
        tipo="Imprensa", artista__nome__range=(select[0], select[1])
    ).order_by("artista")
    return render(request, "publicacoes_imprensa.html", context)


def critica(request, select):
    context = {}
    context["publicacoes"] = Publicacao.objects.filter(
        tipo="Critica", artista__nome__range=(select[0], select[1])
    ).order_by("artista")
    return render(request, "publicacoes_criticas.html", context)
