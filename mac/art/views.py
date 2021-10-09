from django.shortcuts import get_object_or_404, render

from mac.art.models import Artist, ArtWork
from mac.common import common
from mac.gallery.models import Exhibition, Publication


def artist_canvas(artist):
    return artist.canvases.all()


def artistas(request):
    artists = Artist.objects.filter(mac_artist=True).order_by("name")
    context = {"artists": artists}

    # Artists in current Exhibitions. TODO: this can be largely improved
    exposicoes = common.EXPOSICOES
    actuais = [exposicao for exposicao in exposicoes if exposicao.exposicao_actual()]
    artistas_em_exposicao = []
    for exposicao in actuais:
        artistas_em_exposicao.extend(exposicao.artistas.all())
    artistas_em_exposicao = list(set(artistas_em_exposicao))

    context["em_exposicao"] = artistas_em_exposicao

    return render(request, "artistas.html", context)


def artists_filter(art_type_filter):
    return Artist.objects.filter(
        art_type__name=art_type_filter, mac_artist=True
    ).order_by("name")


def pintura(request):
    artists = artists_filter("Pintura")
    return render(request, "artistas_pintura.html", {"artists": artists})


def medalhistica(request):
    artists = artists_filter("Medalhistica")
    return render(request, "artistas_medalhistica.html", {"artists": artists})


def joalharia(request):
    artists = artists_filter("Joalharia")
    return render(request, "artistas_joalharia.html", {"artists": artists})


def escultura(request):
    artists = artists_filter("Escultura")
    return render(request, "artistas_escultura.html", {"artists": artists})


def fotografia(request):
    artists = artists_filter("Fotografia")
    return render(request, "artistas_fotografia.html", {"artists": artists})


def desenho(request):
    artists = artists_filter("Desenho")
    return render(request, "artistas_desenho.html", {"artists": artists})


def ceramica(request):
    artists = artists_filter("Ceramica")
    return render(request, "artistas_ceramica.html", {"artists": artists})


def trofeus(request):
    artists = artists_filter("Trofeus")
    return render(request, "artistas_trofeus.html", {"artists": artists})


def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    works = ArtWork.objects.filter(author=artist_id, state__in=["E", "C"]).order_by(
        "-year"
    )
    collection = ArtWork.objects.filter(author=artist_id, state="A").order_by("-year")
    exhibitions = Exhibition.objects.filter(artists__id__exact=artist.id).order_by(
        "-start_date"
    )
    critics = Publication.objects.filter(
        artist__id__exact=artist.id, publication_type="Critica"
    ).order_by("-date")
    press = Publication.objects.filter(
        artist__id__exact=artist.id, publication_type="Imprensa"
    ).order_by("-date")
    telas = artist_canvas(artist)
    return render(
        request,
        "artistas_detalhe.html",
        {
            "artista": artist,
            "obras": works,
            "telas": telas,
            "exposicoes": exhibitions,
            "imprensa": press,
            "criticas": critics,
            "acervo": collection,
        },
    )


def obras(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    works = ArtWork.objects.filter(author=artist_id, state__in=["C", "E"]).order_by(
        "-year"
    )
    canvases = artist_canvas(artist)
    return render(
        request,
        "artistas_obras.html",
        {"artista": artist, "obras": works, "telas": canvases},
    )


def acervo(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    works = ArtWork.objects.filter(author=artist_id, state="A").order_by("-year")
    canvases = artist_canvas(artist)
    return render(
        request,
        "artistas_acervo.html",
        {"artista": artist, "obras": works, "telas": canvases},
    )


def exposicoes(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    exhibitions = Exhibition.objects.filter(artists__id__exact=artist_id).order_by(
        "-start_date"
    )
    canvases = artist_canvas(artist)
    return render(
        request,
        "artistas_exposicoes.html",
        {"artista": artist, "exposicoes": exhibitions, "telas": canvases},
    )


def critica(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    critics = Publication.objects.filter(
        artist__id__exact=artist_id, publication_type="Critica"
    ).order_by("-date")
    canvases = artist_canvas(artist)
    return render(
        request,
        "artistas_critica.html",
        {"artista": artist, "criticas": critics, "telas": canvases},
    )


def imprensa(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    press = Publication.objects.filter(
        artist__id__exact=artist_id, publication_type="Imprensa"
    ).order_by("-date")
    canvases = artist_canvas(artist)
    return render(
        request,
        "artistas_imprensa.html",
        {"artista": artist, "imprensa": press, "telas": canvases},
    )


def obra_detalhe(request, obra_id, artist_id):
    work = get_object_or_404(ArtWork, pk=obra_id)
    canvases = work.author.canvases.all()
    techniques = work.techniques.all()
    materials = work.materials.all()
    return render(
        request,
        "obra_detalhe.html",
        {
            "obra": work,
            "telas": canvases,
            "tecnicas": techniques,
            "materiais": materials,
            "id_artist": artist_id,
        },
    )
