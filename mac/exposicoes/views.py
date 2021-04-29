from django.shortcuts import get_object_or_404, render

from mac.artistas.models import Obra
from mac.common import common
from mac.exposicoes.models import Exposicao


def index(request):
    exposicoes = common.EXPOSICOES
    actuais = [exposicao for exposicao in exposicoes if exposicao.exposicao_actual()]
    return render(request, "exposicoes_actuais.html", {"exposicoes": actuais})


def passadas(request):
    exposicoes = common.EXPOSICOES
    passadas = [exposicao for exposicao in exposicoes if exposicao.exposicao_passada()]
    anos = list(set([exposicao.data_inicio.year for exposicao in passadas]))
    anos.reverse()
    return render(request, "exposicoes_passadas.html", {"years": anos})


def passadas_ano(request, exposicao_ano):
    exposicoes = Exposicao.objects.filter(data_inicio__year=exposicao_ano)
    passadas = [exposicao for exposicao in exposicoes if exposicao.exposicao_passada()]
    context = {}
    context["exposicoes"] = passadas
    context["ano"] = exposicao_ano
    return render(request, "exposicoes_passadas_ano.html", context)


def futuras(request):
    exposicoes = Exposicao.objects.all().order_by("data_inicio")
    futuras = [exposicao for exposicao in exposicoes if exposicao.exposicao_futura()]
    return render(request, "exposicoes_futuras.html", {"exposicoes": futuras})


def detail(request, exposicao_id):
    exposicao = get_object_or_404(Exposicao, pk=exposicao_id)
    actual = exposicao.exposicao_actual()
    telas = exposicao.telas.all()
    fotos = exposicao.fotos.all()
    galerias = exposicao.galerias.all()
    artistas = exposicao.artistas.all()
    obras = exposicao.obras.all().order_by("-ano")
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
    exposicao = get_object_or_404(Exposicao, pk=exposicao_id)
    obras = exposicao.obras.all().order_by("-ano")
    telas = exposicao.telas.all()
    return render(
        request,
        "exposicoes_obras.html",
        {"exposicao": exposicao, "obras": obras, "telas": telas},
    )


def obra_detalhe(request, exposicao_id, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    exposicao = get_object_or_404(Exposicao, pk=exposicao_id)
    telas = obra.autor.telas.all()
    tecnicas = obra.tecnicas.all()
    materiais = obra.materiais.all()
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
