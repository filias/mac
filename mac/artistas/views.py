# Create your views here.
import random
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models.query import Q
from django.template import RequestContext

from mac.artistas.models import Artista,  Obra
from mac.exposicoes.models import Exposicao
from mac.publicacoes.models import Publicacao
from mac.geral.models import Tela
from mac.utils import utils
from mac.common import common

RTR_DICT = common.DEFAULT_DICT

def artist_canvas(artist):
    return artist.telas.all()

def artistas(request):
    artistas = Artista.objects.filter(artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 3)
    RTR_DICT['artist_list'] = artistas_lista
    # artistas em exposicoes actuais
    exposicoes = common.EXPOSICOES
    actuais = [exposicao for exposicao in exposicoes if exposicao.exposicao_actual()]
    artistas_em_exposicao = []
    for exposicao in actuais:
        artistas_em_exposicao.extend(exposicao.artistas.all())
    artistas_em_exposicao = list(set(artistas_em_exposicao))
    
    RTR_DICT['em_exposicao'] = artistas_em_exposicao
    return render_to_response('artistas/templates/artistas.html', RTR_DICT, context_instance=RequestContext(request))
    
def pintura(request):
    artistas = Artista.objects.filter(tipo__nome=u'Pintura', artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 3)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_pintura.html', RTR_DICT, context_instance=RequestContext(request))

def medalhistica(request):
    artistas = Artista.objects.filter(tipo__nome=u'Medalhistica', artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 3)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_medalhistica.html', RTR_DICT, context_instance=RequestContext(request))
    
def joalharia(request):
    artistas = Artista.objects.filter(tipo__nome=u'Joalharia', artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 1)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_joalharia.html', RTR_DICT, context_instance=RequestContext(request))

def escultura(request):
    artistas = Artista.objects.filter(tipo__nome=u'Escultura', artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 1)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_escultura.html', RTR_DICT, context_instance=RequestContext(request))

def fotografia(request):
    artistas = Artista.objects.filter(tipo__nome=u'Fotografia', artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 1)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_fotografia.html', RTR_DICT, context_instance=RequestContext(request))

def desenho(request):
    artistas = Artista.objects.filter(tipo__nome=u'Desenho', artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 1)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_desenho.html', RTR_DICT, context_instance=RequestContext(request))

def ceramica(request):
    artistas = Artista.objects.filter(tipo__nome=u'Ceramica', artista_mac=True).order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 1)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_ceramica.html', RTR_DICT, context_instance=RequestContext(request))

def trofeus(request):
    artistas = Artista.objects.filter(tipo__nome=u'Trofeus').order_by('nome')
    artistas_lista = utils.arrange_by_columns(list(artistas), 1)
    RTR_DICT['artist_list'] = artistas_lista
    return render_to_response('artistas/templates/artistas_trofeus.html', RTR_DICT, context_instance=RequestContext(request))

def detail(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    obras = Obra.objects.filter(autor=artist_id, estado__in=['E', 'C']).order_by('-ano')
    acervo = Obra.objects.filter(autor=artist_id, estado='A').order_by('-ano')
    exposicoes = Exposicao.objects.filter(artistas__id__exact=artista.id).order_by('-data_inicio')
    criticas = Publicacao.objects.filter(artista__id__exact=artista.id, tipo='Critica').order_by('-data')
    imprensa = Publicacao.objects.filter(artista__id__exact=artista.id, tipo='Imprensa').order_by('-data')
    telas = artist_canvas(artista)
    return render_to_response('artistas/templates/artistas_detalhe.html', {'artista': artista, 'obras': obras, 'telas': telas, 'exposicoes': exposicoes, 'imprensa': imprensa, 'criticas': criticas,  'acervo':acervo}, context_instance=RequestContext(request))

def obras(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    obras = Obra.objects.filter(autor=artist_id, estado__in=['C', 'E']).order_by('-ano')
    telas = artist_canvas(artista)
    return render_to_response('artistas/templates/artistas_obras.html', {'artista': artista, 'obras': obras, 'telas': telas}, context_instance=RequestContext(request))

def acervo(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    obras = Obra.objects.filter(autor=artist_id, estado='A').order_by('-ano')
    telas = artist_canvas(artista)
    return render_to_response('artistas/templates/artistas_acervo.html', {'artista': artista, 'obras': obras, 'telas': telas}, context_instance=RequestContext(request))

def exposicoes(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    exposicoes = Exposicao.objects.filter(artistas__id__exact=artista.id).order_by('-data_inicio')
    telas = artist_canvas(artista)
    return render_to_response('artistas/templates/artistas_exposicoes.html', {'artista': artista, 'exposicoes': exposicoes, 'telas': telas}, context_instance=RequestContext(request))

def critica(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    criticas = Publicacao.objects.filter(artista__id__exact=artista.id, tipo='Critica').order_by('-data')
    telas = artist_canvas(artista)
    return render_to_response('artistas/templates/artistas_critica.html', {'artista': artista, 'criticas': criticas, 'telas': telas}, context_instance=RequestContext(request))

def imprensa(request, artist_id):
    artista = get_object_or_404(Artista, pk=artist_id)
    imprensa = Publicacao.objects.filter(artista__id__exact=artista.id, tipo='Imprensa').order_by('-data')
    telas = artist_canvas(artista)
    return render_to_response('artistas/templates/artistas_imprensa.html', {'artista': artista, 'imprensa': imprensa, 'telas': telas}, context_instance=RequestContext(request))

def obra_detalhe(request, obra_id,  artist_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    telas = obra.autor.telas.all()
    tecnicas = obra.tecnicas.all()
    materiais = obra.materiais.all()
    return render_to_response('artistas/templates/obra_detalhe.html', {'obra': obra, 'telas': telas, 'tecnicas': tecnicas, 'materiais': materiais}, context_instance=RequestContext(request))
    
