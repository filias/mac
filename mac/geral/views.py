from django.http import HttpResponseRedirect
from django.shortcuts import render

from mac.geral.forms import ContactForm


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
