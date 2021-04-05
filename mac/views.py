from django import http
from django.conf import settings
from django.shortcuts import render
from django.utils.translation import check_for_language

from mac.common import common
from mac.publicacoes.models import Link

RTR_DICT = common.DEFAULT_DICT


def set_language(request, lang_code):
    breakpoint()
    next = request.REQUEST.get("next", None)
    if not next:
        next = "/"
    response = http.HttpResponseRedirect(next)
    if lang_code and check_for_language(lang_code):
        if hasattr(request, "session"):
            request.session["django_language"] = lang_code
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response


def resultados(request):
    return render(request, "templates/resultados.html", RTR_DICT)


def arte(request):
    return render(request, "templates/arte.html", RTR_DICT)


def servicos(request):
    return render(request, "templates/servicos.html", RTR_DICT)


def mapa(request):
    return render(request, "templates/mapa.html", RTR_DICT)


def links(request):
    RTR_DICT["links_list"] = Link.objects.all()
    return render(request, "templates/links.html", RTR_DICT)
