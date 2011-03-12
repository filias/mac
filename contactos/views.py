from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from mac.contactos.models import ContactForm
from mac.galeria.models import Galeria
from mac.geral.models import Tela
from mac.common import common

RTR_DICT = common.DEFAULT_DICT

# Create your views here.
def contactos(request):
    gallery_list = Galeria.objects.filter(nome__startswith='MAC').order_by('-nome')
    RTR_DICT['gallery_list'] = gallery_list
    return render_to_response('contactos/templates/contactos.html', RTR_DICT, context_instance=RequestContext(request))

def contacte_nos(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
#            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['mac@movimentoartecontemporanea.com']
            recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('sucesso') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    
    RTR_DICT['form'] = form
    return render_to_response('contactos/templates/contacte_nos.html', RTR_DICT, context_instance=RequestContext(request))

def sucesso(request):
    return render_to_response('contactos/templates/contactos_sucesso.html', RTR_DICT, context_instance=RequestContext(request))
