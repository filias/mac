import random

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import never_cache

from mac.artistas.models import Artista, Obra
from mac.exposicoes.models import Exposicao
from mac.galeria.models import Aniversario, Galeria, Premio
from mac.geral.models import Destaque, Tela
from mac.publicacoes.models import Texto


def index(request):
    destaques = Destaque.objects.filter(visivel=True).order_by("ordem")
    return render(request, "templates/index.html", {"destaques": destaques})


@never_cache
def tela(request):
    telas_list = Tela.objects.all()
    telas = []
    for tela_completa in telas_list:
        telas.append(tela_completa.image)
    tela = random.choice(telas)
    return HttpResponse("%s%s" % ("/site-media/", str(tela)), mimetype="text/plain")


def galerias(request):
    galerias = Galeria.objects.filter(nome__startswith="MAC").order_by("-nome")
    return render(request, "galeria.html", {"galerias": galerias})


def missao(request):
    texto = Texto.objects.filter(titulo="missao")
    return render(request, "galeria_missao.html", {"texto": texto[0]})


def historia(request):
    texto = Texto.objects.filter(titulo="historia")
    return render(request, "galeria_historia.html", {"texto": texto[0]})


def curriculum(request):
    exposicoes = Exposicao.objects.all()
    years = list(set([exposicao.data_inicio.year for exposicao in exposicoes]))
    years.reverse()

    return render(request, "galeria_curriculum.html", {"years": years})


def curriculum_ano(request, evento_ano):
    eventos = Exposicao.objects.filter(data_inicio__year=evento_ano)
    context = {}
    context["eventos"] = eventos
    context["ano"] = evento_ano
    return render(request, "galeria/templates/galeria_curriculum_anos.html", context)


def equipa(request):
    texto = Texto.objects.filter(titulo="estrutura")
    return render(request, "galeria_equipa.html", {"texto": texto[0]})


def acervo(request):
    artistas = Artista.objects.all().order_by("nome")
    artists = [artista for artista in artistas if artista.tem_acervo()]
    return render(request, "galeria_acervo.html", {"artists": artists})


def acervo_artist(request, artist_id):
    artista = Artista.objects.get(pk=artist_id)
    telas = artista.telas.all()
    acervo_list = Obra.objects.filter(estado="A", autor=artista).order_by("-ano")
    return render(
        request,
        "galeria_acervo_artista.html",
        {"artista": artista, "telas": telas, "acervo_list": acervo_list},
    )


def acervo_detalhe(request, obra_id, artist_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    telas = obra.autor.telas.all()
    tecnicas = obra.tecnicas.all()
    materiais = obra.materiais.all()

    return render(
        request,
        "acervo_detalhe.html",
        {"obra": obra, "telas": telas, "tecnicas": tecnicas, "materiais": materiais},
    )


def agenda(request):
    return render(request, "galeria_agenda.html")


def premios(request):
    texto = Texto.objects.filter(titulo="premios")
    context = {}
    context["texto"] = texto[0]
    aniversarios = Aniversario.objects.all().order_by("-data")
    context["aniversarios"] = aniversarios
    return render(request, "galeria_premios.html", context)


def detail(request, aniversario_id):
    aniversario = get_object_or_404(Aniversario, pk=aniversario_id)
    context = {}
    context["aniversario"] = aniversario
    fotos = aniversario.fotos.all()
    context["fotos"] = fotos
    premios = Premio.objects.filter(aniversario=aniversario_id).order_by("nome")
    context["premios"] = premios
    return render(request, "premios_detalhe.html", context)


def premiados(request, aniversario_id):
    aniversario = get_object_or_404(Aniversario, pk=aniversario_id)
    context = {}
    context["aniversario"] = aniversario
    premios = Premio.objects.filter(aniversario=aniversario_id).order_by("nome")
    context["premios"] = premios
    return render(request, "premiados.html", context)


def trofeu(request, aniversario_id):
    aniversario = get_object_or_404(Aniversario, pk=aniversario_id)
    trofeu = aniversario.trofeu
    telas = trofeu.autor.telas.all()
    tecnicas = trofeu.tecnicas.all()
    materiais = trofeu.materiais.all()
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
