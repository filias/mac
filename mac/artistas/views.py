from django.shortcuts import get_object_or_404, render

from mac.artistas.models import Artista, Obra
from mac.common import common
from mac.exposicoes.models import Exposicao
from mac.publicacoes.models import Publicacao


def artist_canvas(artist):
    return artist.telas.all()


def artistas(request):
    artistas = Artista.objects.filter(artista_mac=True).order_by("nome")
    context = {}
    context["artists"] = artistas

    # Artists in current Exhibitions. TODO: this can be largely improved
    exposicoes = common.EXPOSICOES
    actuais = [exposicao for exposicao in exposicoes if exposicao.exposicao_actual()]
    artistas_em_exposicao = []
    for exposicao in actuais:
        artistas_em_exposicao.extend(exposicao.artistas.all())
    artistas_em_exposicao = list(set(artistas_em_exposicao))

    context["em_exposicao"] = artistas_em_exposicao

    return render(request, "artistas.html", context)


def pintura(request):
    artistas = Artista.objects.filter(tipo__nome="Pintura", artista_mac=True).order_by(
        "nome"
    )

    return render(request, "artistas_pintura.html", {"artists": artistas})


def medalhistica(request):
    artistas = Artista.objects.filter(
        tipo__nome="Medalhistica", artista_mac=True
    ).order_by("nome")

    return render(request, "artistas_medalhistica.html", {"artists": artistas})


def joalharia(request):
    artistas = Artista.objects.filter(
        tipo__nome="Joalharia", artista_mac=True
    ).order_by("nome")

    return render(request, "artistas_joalharia.html", {"artists": artistas})


def escultura(request):
    artistas = Artista.objects.filter(
        tipo__nome="Escultura", artista_mac=True
    ).order_by("nome")

    return render(request, "artistas_escultura.html", {"artists": artistas})


def fotografia(request):
    artistas = Artista.objects.filter(
        tipo__nome="Fotografia", artista_mac=True
    ).order_by("nome")

    return render(request, "artistas_fotografia.html", {"artists": artistas})


def desenho(request):
    artistas = Artista.objects.filter(tipo__nome=u"Desenho", artista_mac=True).order_by(
        "nome"
    )

    return render(request, "artistas_desenho.html", {"artists": artistas})


def ceramica(request):
    artistas = Artista.objects.filter(tipo__nome="Ceramica", artista_mac=True).order_by(
        "nome"
    )

    return render(request, "artistas_ceramica.html", {"artists": artistas})


def trofeus(request):
    artistas = Artista.objects.filter(tipo__nome="Trofeus").order_by("nome")

    return render(request, "artistas_trofeus.html", {"artists": artistas})


def detail(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    obras = Obra.objects.filter(autor=artist_id, estado__in=["E", "C"]).order_by("-ano")
    acervo = Obra.objects.filter(autor=artist_id, estado="A").order_by("-ano")
    exposicoes = Exposicao.objects.filter(artistas__id__exact=artista.id).order_by(
        "-data_inicio"
    )
    criticas = Publicacao.objects.filter(
        artista__id__exact=artista.id, tipo="Critica"
    ).order_by("-data")
    imprensa = Publicacao.objects.filter(
        artista__id__exact=artista.id, tipo="Imprensa"
    ).order_by("-data")
    telas = artist_canvas(artista)
    return render(
        request,
        "artistas_detalhe.html",
        {
            "artista": artista,
            "obras": obras,
            "telas": telas,
            "exposicoes": exposicoes,
            "imprensa": imprensa,
            "criticas": criticas,
            "acervo": acervo,
        },
    )


def obras(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    obras = Obra.objects.filter(autor=artist_id, estado__in=["C", "E"]).order_by("-ano")
    telas = artist_canvas(artista)
    return render(
        request,
        "artistas_obras.html",
        {"artista": artista, "obras": obras, "telas": telas},
    )


def acervo(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    obras = Obra.objects.filter(autor=artist_id, estado="A").order_by("-ano")
    telas = artist_canvas(artista)
    return render(
        request,
        "artistas_acervo.html",
        {"artista": artista, "obras": obras, "telas": telas},
    )


def exposicoes(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    exposicoes = Exposicao.objects.filter(artistas__id__exact=artista.id).order_by(
        "-data_inicio"
    )
    telas = artist_canvas(artista)
    return render(
        request,
        "artistas_exposicoes.html",
        {"artista": artista, "exposicoes": exposicoes, "telas": telas},
    )


def critica(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    criticas = Publicacao.objects.filter(
        artista__id__exact=artista.id, tipo="Critica"
    ).order_by("-data")
    telas = artist_canvas(artista)
    return render(
        request,
        "artistas_critica.html",
        {"artista": artista, "criticas": criticas, "telas": telas},
    )


def imprensa(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    imprensa = Publicacao.objects.filter(
        artista__id__exact=artista.id, tipo="Imprensa"
    ).order_by("-data")
    telas = artist_canvas(artista)
    return render(
        request,
        "artistas_imprensa.html",
        {"artista": artista, "imprensa": imprensa, "telas": telas},
    )


def obra_detalhe(request, obra_id, artist_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    telas = obra.autor.telas.all()
    tecnicas = obra.tecnicas.all()
    materiais = obra.materiais.all()
    return render(
        request,
        "obra_detalhe.html",
        {"obra": obra, "telas": telas, "tecnicas": tecnicas, "materiais": materiais, "id_artist":artist_id},
    )
