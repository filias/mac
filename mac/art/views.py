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
        artists_in_exhibition.add(exhibition.artists.all())

    return list(set(artists_in_exhibition))


def artists(request):
    # Get all artists
    artists = Artist.objects.filter(mac_artist=True).order_by("name")
    context = {}

    # Filter by art type
    art_type = request.GET.get("type")
    if art_type:
        artists = artists.filter(art_type__name=art_type)
        context["art_type"] = art_type

    context["artists"] = artists

    return render(request, "artists.html", context)


def artists_filter(art_type_filter):
    return Artist.objects.filter(
        art_type__name=art_type_filter, mac_artist=True
    ).order_by("name")


def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    works = artist.artwork_set.filter(state__in=["E", "C"]).order_by("-year")
    collection = artist.artwork_set.filter(state="A").order_by("-year")
    exhibitions = Exhibition.objects.filter(artists__id__exact=artist.id).order_by(
        "-start_date"
    )
    critics = artist.publication_set.filter(publication_type="Critica").order_by("-date")
    press = artist.publication_set.filter(publication_type="Imprensa").order_by("-date")
    canvases = artist_canvas(artist)

    return render(
        request,
        "artist_detail.html",
        {
            "artist": artist,
            "works": works,
            "canvases": canvases,
            "exhibitions": exhibitions,
            "press": press,
            "critics": critics,
            "collection": collection,
        },
    )


def works(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    works = artist.artwork_set.filter(state__in=["C", "E"]).order_by("-year")
    canvases = artist_canvas(artist)
    return render(
        request,
        "artist_works.html",
        {"artist": artist, "works": works, "canvases": canvases},
    )


def collection(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    works = ArtWork.objects.filter(author=artist_id, state="A").order_by("-year")
    canvases = artist_canvas(artist)
    return render(
        request,
        "artist_collection.html",
        {"artist": artist, "works": works, "canvases": canvases},
    )


def exhibitions(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    exhibitions = Exhibition.objects.filter(artists__id__exact=artist_id).order_by(
        "-start_date"
    )
    canvases = artist_canvas(artist)
    return render(
        request,
        "artist_exhibitions.html",
        {"artist": artist, "exhibitions": exhibitions, "canvases": canvases},
    )


def critics(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    critics = Publication.objects.filter(
        artist__id__exact=artist_id, publication_type="Critica"
    ).order_by("-date")
    canvases = artist_canvas(artist)
    return render(
        request,
        "artist_critics.html",
        {"artist": artist, "critics": critics, "canvases": canvases},
    )


def press(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    press = Publication.objects.filter(
        artist__id__exact=artist_id, publication_type="Imprensa"
    ).order_by("-date")
    canvases = artist_canvas(artist)
    return render(
        request,
        "artist_press.html",
        {"artist": artist, "press": press, "canvases": canvases},
    )


def work_detail(request, obra_id, artist_id):
    work = get_object_or_404(ArtWork, pk=obra_id)
    canvases = work.author.canvases.all()
    techniques = work.techniques.all()
    materials = work.materials.all()
    return render(
        request,
        "work_detail.html",
        {
            "work": work,
            "canvases": canvases,
            "techniques": techniques,
            "materials": materials,
            "artist_id": artist_id,
        },
    )
