from django.shortcuts import get_object_or_404, render

from mac.art.models import Artist, ArtWork
from mac.gallery.models import Exhibition, Publication


def artist_canvas(artist):
    return artist.canvases.all()


def artists_in_exhibition():
    """Artists in current Exhibitions"""
    # TODO: check if this should be used
    exhibitions = Exhibition.objects.all()

    # TODO: make a manager for this
    current_exhibitions = [exhibition for exhibition in exhibitions if exhibition.is_current]
    artists_in_exhibition = []
    for exhibition in current_exhibitions:
        artists_in_exhibition.add(exhibition.artistas.all())

    return list(set(artists_in_exhibition))


def artistas(request):
    # Get all artists
    artists = Artist.objects.filter(mac_artist=True).order_by("name")
    context = {}

    # Filter by art type
    art_type = request.GET.get("type")
    if art_type:
        artists = artists.filter(art_type__name=art_type)
        context["art_type"] = art_type

    context["artists"] = artists

    return render(request, "artistas.html", context)


def artists_filter(art_type_filter):
    return Artist.objects.filter(
        art_type__name=art_type_filter, mac_artist=True
    ).order_by("name")


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
