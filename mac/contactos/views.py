from django.http import HttpResponseRedirect
from django.shortcuts import render

from mac.common import common
from mac.contactos.models import ContactForm
from mac.galeria.models import Galeria

RTR_DICT = common.DEFAULT_DICT


def contactos(request):
    gallery_list = Galeria.objects.filter(nome__startswith="MAC").order_by("-nome")
    RTR_DICT["gallery_list"] = gallery_list
    return render(request, "contactos/templates/contactos.html", RTR_DICT)


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

    RTR_DICT["form"] = form
    return render(request, "contactos/templates/contacte_nos.html", RTR_DICT)


def sucesso(request):
    return render(request, "contactos/templates/contactos_sucesso.html", RTR_DICT)
