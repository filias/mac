from random import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import never_cache

from mac.art.models import Artist, ArtWork, Canvas
from mac.gallery.forms import ContactForm
from mac.gallery.models import (
    Anniversary,
    Award,
    Exhibition,
    Gallery,
    Publication,
    Snippet,
    Text,
)


def index(request):
    destaques = Snippet.objects.filter(is_visible=True).order_by("ordering")
    return render(request, "templates/index.html", {"destaques": destaques})


@never_cache
def tela(request):
    telas_list = Canvas.objects.all()
    telas = []
    for tela_completa in telas_list:
        telas.append(tela_completa.image)
    tela = random.choice(telas)
    return HttpResponse("%s%s" % ("/site-media/", str(tela)), mimetype="text/plain")


def galerias(request):
    galerias = Gallery.objects.filter(name__startswith="MAC").order_by("-name")
    return render(request, "galeria.html", {"galerias": galerias})


def missao(request):
    texto = Text.objects.filter(title="missao")
    return render(request, "galeria_missao.html", {"texto": texto[0]})


def historia(request):
    texto = Text.objects.filter(title="historia")
    return render(request, "galeria_historia.html", {"texto": texto[0]})


def curriculum(request):
    exposicoes = Exhibition.objects.all()
    years = list(set([exposicao.start_date.year for exposicao in exposicoes]))
    years.reverse()

    return render(request, "galeria_curriculum.html", {"years": years})


def curriculum_ano(request, evento_ano):
    eventos = Exhibition.objects.filter(start_date__year=evento_ano)
    context = {}
    context["eventos"] = eventos
    context["ano"] = evento_ano
    return render(request, "galeria_curriculum_anos.html", context)


def equipa(request):
    texto = Text.objects.filter(title="estrutura")
    return render(request, "galeria_equipa.html", {"texto": texto[0]})


def acervo(request):
    artistas = Artist.objects.all().order_by("name")
    artists = [artista for artista in artistas if artista.tem_acervo()]
    return render(request, "galeria_acervo.html", {"artists": artists})


def acervo_artist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    canvases = artist.canvases.all()
    acervo_list = ArtWork.objects.filter(state="A", author=artist).order_by("-year")
    return render(
        request,
        "galeria_acervo_artista.html",
        {"artista": artist, "telas": canvases, "acervo_list": acervo_list},
    )


def acervo_detalhe(request, obra_id, artist_id):
    obra = get_object_or_404(ArtWork, pk=obra_id)
    telas = obra.author.canvases.all()
    tecnicas = obra.techniques.all()
    materiais = obra.materials.all()

    return render(
        request,
        "acervo_detalhe.html",
        {"obra": obra, "telas": telas, "tecnicas": tecnicas, "materiais": materiais},
    )


def agenda(request):
    return render(request, "galeria_agenda.html")


def premios(request):
    texto = Text.objects.filter(title="premios")
    context = {}
    context["texto"] = texto[0]
    aniversarios = Anniversary.objects.all().order_by("-date")
    context["aniversarios"] = aniversarios
    return render(request, "galeria_premios.html", context)


def anniversary_detail(request, aniversario_id):
    aniversario = get_object_or_404(Anniversary, pk=aniversario_id)
    context = {}
    context["aniversario"] = aniversario
    fotos = aniversario.fotos.all()
    context["fotos"] = fotos
    premios = Award.objects.filter(anniversary=aniversario_id).order_by("name")
    context["premios"] = premios
    return render(request, "premios_detalhe.html", context)


def premiados(request, aniversario_id):
    aniversario = get_object_or_404(Anniversary, pk=aniversario_id)
    context = {}
    context["aniversario"] = aniversario
    premios = Award.objects.filter(anniversary=aniversario_id).order_by("name")
    context["premios"] = premios
    return render(request, "premiados.html", context)


def trofeu(request, aniversario_id):
    aniversario = get_object_or_404(Anniversary, pk=aniversario_id)
    trofeu = aniversario.trophy
    telas = trofeu.author.canvases.all()
    tecnicas = trofeu.techniques.all()
    materiais = trofeu.materials.all()
    return render(
        request,
        "trofeu.html",
        {
            "aniversario": aniversario,
            "trofeu": trofeu,
            "telas": telas,
            "tecnicas": tecnicas,
            "materiais": materiais,
        },
    )


def exhibitions(request):
    exposicoes = Exhibition.objects.all()
    actuais = [exposicao for exposicao in exposicoes if exposicao.is_current]
    return render(request, "exposicoes_actuais.html", {"exposicoes": actuais})


def passadas(request):
    exposicoes = Exhibition.objects.all()
    passadas = [exposicao for exposicao in exposicoes if exposicao.is_past]
    anos = list(set([exposicao.start_date.year for exposicao in passadas]))
    anos.reverse()
    return render(request, "exposicoes_passadas.html", {"years": anos})


def passadas_ano(request, exposicao_ano):
    exposicoes = Exhibition.objects.filter(start_date__year=exposicao_ano)
    passadas = [exposicao for exposicao in exposicoes if exposicao.is_past]
    context = {}
    context["exposicoes"] = passadas
    context["ano"] = exposicao_ano
    return render(request, "exposicoes_passadas_ano.html", context)


def futuras(request):
    exposicoes = Exhibition.objects.all().order_by("start_date")
    futuras = [exposicao for exposicao in exposicoes if exposicao.is_future]
    return render(request, "exposicoes_futuras.html", {"exposicoes": futuras})


def detail(request, exposicao_id):
    exposicao = get_object_or_404(Exhibition, pk=exposicao_id)
    actual = exposicao.exposicao_actual()
    telas = exposicao.canvases.all()
    fotos = exposicao.fotos.all()
    galerias = exposicao.galleries.all()
    artistas = exposicao.artists.all()
    obras = exposicao.art_works.all().order_by("-year")
    return render(
        request,
        "exposicoes_detalhe.html",
        {
            "actual": actual,
            "exposicao": exposicao,
            "telas": telas,
            "fotos": fotos,
            "galerias": galerias,
            "artistas": artistas,
            "obras": obras,
        },
    )


def obras(request, exposicao_id):
    exposicao = get_object_or_404(Exhibition, pk=exposicao_id)
    obras = exposicao.art_works.all().order_by("-year")
    telas = exposicao.canvases.all()
    return render(
        request,
        "exposicoes_obras.html",
        {"exposicao": exposicao, "obras": obras, "telas": telas},
    )


def obra_detalhe(request, exposicao_id, obra_id):
    obra = get_object_or_404(ArtWork, pk=obra_id)
    exposicao = get_object_or_404(Exhibition, pk=exposicao_id)
    telas = obra.author.canvases.all()
    tecnicas = obra.techniques.all()
    materiais = obra.materials.all()
    return render(
        request,
        "obra_detalhe.html",
        {
            "obra": obra,
            "telas": telas,
            "tecnicas": tecnicas,
            "materiais": materiais,
            "exposicao": exposicao,
        },
    )


def catalogos(request, select):
    context = {}
    context["publicacoes"] = Publication.objects.filter(
        publication_type="Catalogo", artist__name__range=(select[0], select[1])
    ).order_by("artist")
    return render(request, "publicacoes_catalogos.html", context)


def imprensa(request, select):
    context = {}
    context["publicacoes"] = Publication.objects.filter(
        publication_type="Imprensa", artist__name__range=(select[0], select[1])
    ).order_by("artist")
    return render(request, "publicacoes_imprensa.html", context)


def critica(request, select):
    context = {}
    context["publicacoes"] = Publication.objects.filter(
        publication_type="Critica", artist__name__range=(select[0], select[1])
    ).order_by("artist")
    return render(request, "publicacoes_criticas.html", context)


def contactos(request):
    return render(request, "contactos.html")


def contacte_nos(request):
    if request.method == "POST":  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            recipients = ["mac@movimentoartecontemporanea.com"]
            recipients.append(sender)

            from django.core.mail import send_mail

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect("sucesso")  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    return render(request, "contacte_nos.html", {"form": form})


def sucesso(request):
    return render(request, "contactos_sucesso.html")
