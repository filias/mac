from django.shortcuts import render

from mac.publicacoes.models import Link


def resultados(request):
    return render(request, "templates/resultados.html")


def mapa(request):
    return render(request, "templates/mapa.html")


def links(request):
    return render(request, "templates/links.html", {"links_list": Link.objects.all()})
