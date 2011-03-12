import random
from django.views.decorators.cache import never_cache
from django import http
from django.utils.translation import check_for_language
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

from mac.galeria.models import Galeria
from mac.geral.models import Tela
from mac.publicacoes.models import Link, Texto
from mac.common import common

RTR_DICT = common.DEFAULT_DICT

def set_language(request, lang_code):
    next = request.REQUEST.get('next', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response 
    
def resultados(request):
    return render_to_response('templates/resultados.html', RTR_DICT, context_instance=RequestContext(request))

def arte(request):
    return render_to_response('templates/arte.html', RTR_DICT, context_instance=RequestContext(request))

def servicos(request):
    return render_to_response('templates/servicos.html', RTR_DICT, context_instance=RequestContext(request))

def mapa(request):
    return render_to_response('templates/mapa.html', RTR_DICT, context_instance=RequestContext(request))
                
def links(request):
    RTR_DICT['links_list'] = Link.objects.all()
    return render_to_response('templates/links.html', RTR_DICT, context_instance=RequestContext(request))
