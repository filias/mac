from django.shortcuts import get_object_or_404, render

from mac.exposicoes.models import Exposicao
from mac.artistas.models import Obra

from mac.common import common
from mac.utils import utils

RTR_DICT = common.DEFAULT_DICT


def index(request):
    exposicoes = common.EXPOSICOES
    actuais = [exposicao for exposicao in exposicoes if exposicao.exposicao_actual()]
    RTR_DICT["exposicoes"] = actuais
    return render(request, "exposicoes/templates/exposicoes_actuais.html", RTR_DICT)


def passadas(request):
    exposicoes = common.EXPOSICOES
    passadas = [exposicao for exposicao in exposicoes if exposicao.exposicao_passada()]
    anos = set([exposicao.data_inicio.year for exposicao in passadas])
    anos = list(anos)
    anos.reverse()
    anos = utils.arrange_by_columns(anos, 2)
    RTR_DICT["anos"] = anos
    return render(request, "exposicoes/templates/exposicoes_passadas.html", RTR_DICT)


def passadas_ano(request, exposicao_ano):
    exposicoes = Exposicao.objects.filter(data_inicio__year=exposicao_ano)
    passadas = [exposicao for exposicao in exposicoes if exposicao.exposicao_passada()]
    RTR_DICT["exposicoes"] = passadas
    RTR_DICT["ano"] = exposicao_ano
    return render(
        request, "exposicoes/templates/exposicoes_passadas_ano.html", RTR_DICT
    )


def futuras(request):
    exposicoes = Exposicao.objects.all().order_by("data_inicio")
    futuras = [exposicao for exposicao in exposicoes if exposicao.exposicao_futura()]
    RTR_DICT["exposicoes"] = futuras
    return render(request, "exposicoes/templates/exposicoes_futuras.html", RTR_DICT)


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
        "exposicoes/templates/exposicoes_detalhe.html",
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
        "exposicoes/templates/exposicoes_obras.html",
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
        "exposicoes/templates/obra_detalhe.html",
        {
            "obra": obra,
            "telas": telas,
            "tecnicas": tecnicas,
            "materiais": materiais,
            "exposicao": exposicao,
        },
    )
