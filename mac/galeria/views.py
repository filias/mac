import random

from django.shortcuts import get_object_or_404
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from django.shortcuts import render

from mac.artistas.models import Obra, Artista
from mac.galeria.models import Galeria, Staff, Premio, Aniversario, Premiado
from mac.geral.models import Tela, Destaque
from mac.publicacoes.models import Texto
from mac.exposicoes.models import Exposicao
from mac.utils import utils
from mac.common import common

RTR_DICT = common.DEFAULT_DICT

def index(request):
    destaques = Destaque.objects.filter(visivel=True).order_by('ordem')
    RTR_DICT['destaques'] = destaques
    return render(request, 'templates/index.html', RTR_DICT)

@never_cache
def tela(request):
    telas_list = Tela.objects.all()
    telas = []
    for tela_completa in telas_list:
        telas.append(tela_completa.image)
    tela = random.choice(telas)
    return HttpResponse('%s%s' % ('/site-media/', str(tela)), mimetype='text/plain')

def galerias(request):
    galerias = Galeria.objects.filter(nome__startswith='MAC').order_by('-nome')
    RTR_DICT['galerias'] = galerias
    return render(request, 'galeria/templates/galeria.html', RTR_DICT)

def missao(request):
    texto = Texto.objects.filter(titulo='missao')
    RTR_DICT['texto'] = texto[0]
    return render(request, 'galeria/templates/galeria_missao.html', RTR_DICT)

def historia(request):
    texto = Texto.objects.filter(titulo='historia')
    RTR_DICT['texto'] = texto[0]
    return render(request, 'galeria/templates/galeria_historia.html', RTR_DICT)

def curriculum(request):
    exposicoes = Exposicao.objects.all()
    anos = set([exposicao.data_inicio.year for exposicao in exposicoes])
    anos = list(anos)
    anos.reverse()
    anos = utils.arrange_by_columns(anos, 2)
    RTR_DICT['anos'] = anos
    return render(request, 'galeria/templates/galeria_curriculum.html', RTR_DICT)
    
def curriculum_ano(request, evento_ano):
    eventos = Exposicao.objects.filter(data_inicio__year=evento_ano)
    RTR_DICT['eventos'] = eventos
    RTR_DICT['ano'] =evento_ano
    return render(request, 'galeria/templates/galeria_curriculum_anos.html', RTR_DICT)
    
def equipa(request):
    texto = Texto.objects.filter(titulo='estrutura')
    RTR_DICT['texto'] = texto[0]
    return render(request, 'galeria/templates/galeria_equipa.html', RTR_DICT)

def acervo(request):
    artistas = Artista.objects.all().order_by('nome')
    artistas = [artista for artista in artistas if artista.tem_acervo()]
    artistas_lista = utils.arrange_by_columns(list(artistas), 3)
    RTR_DICT['artist_list'] = artistas_lista
    return render(request, 'galeria/templates/galeria_acervo.html', RTR_DICT)

def acervo_artist(request, artist_id):
    artista = Artista.objects.get(pk=artist_id)
    telas = artista.telas.all()
    acervo_list = Obra.objects.filter(estado='A', autor=artista).order_by('-ano')
    return render(request, 'galeria/templates/galeria_acervo_artista.html', {'artista': artista, 'telas': telas, 'acervo_list':acervo_list})

def acervo_detalhe(request, obra_id,  artist_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    telas = obra.autor.telas.all()
    tecnicas = obra.tecnicas.all()
    materiais = obra.materiais.all()

    return render(request, 'galeria/templates/acervo_detalhe.html', {'obra': obra, 'telas': telas, 'tecnicas': tecnicas, 'materiais': materiais})

def visita(request):
    return render(request, 'galeria/templates/galeria_visita.html', RTR_DICT)

def agenda(request):
    return render(request, 'galeria/templates/galeria_agenda.html', RTR_DICT)

def premios(request):
    texto = Texto.objects.filter(titulo='premios')
    RTR_DICT['texto'] = texto[0]
    aniversarios = Aniversario.objects.all().order_by('-data')
    RTR_DICT['aniversarios'] = aniversarios
    return render(request, 'galeria/templates/galeria_premios.html', RTR_DICT)

def detail(request, aniversario_id):
    aniversario = get_object_or_404(Aniversario, pk=aniversario_id)
    RTR_DICT['aniversario'] = aniversario
    fotos = aniversario.fotos.all()
    RTR_DICT['fotos'] = fotos
    premios = Premio.objects.filter(aniversario=aniversario_id).order_by('nome')
    RTR_DICT['premios'] = premios
    return render(request, 'galeria/templates/premios_detalhe.html', RTR_DICT)

def premiados(request, aniversario_id):
    aniversario = get_object_or_404(Aniversario, pk=aniversario_id)
    RTR_DICT['aniversario'] = aniversario
    premios = Premio.objects.filter(aniversario=aniversario_id).order_by('nome')
    RTR_DICT['premios'] = premios
    return render(request, 'galeria/templates/premiados.html', RTR_DICT)

def trofeu(request, aniversario_id):
    aniversario = get_object_or_404(Aniversario, pk=aniversario_id)
    trofeu = aniversario.trofeu
    telas = trofeu.autor.telas.all()
    tecnicas = trofeu.tecnicas.all()
    materiais = trofeu.materiais.all()
    return render(request, 'galeria/templates/trofeu.html', {'aniversario': aniversario, 'trofeu': trofeu, 'telas': telas, 'tecnicas': tecnicas, 'materiais': materiais})
