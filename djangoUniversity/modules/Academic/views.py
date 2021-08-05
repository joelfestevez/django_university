from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def formularioContacto(request):
    return render(request,"formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto=request.POST['txtAsunto']
        mensaje=request.POST['txtMensaje']+" / Email: "+request.POST['txtEmail']
        email_desde=settings.EMAIL_HOST_USER
        email_para=['joelito.402@gmail.com']
        send_mail(asunto, mensaje, email_desde,email_para, fail_silently=False) #Este fail sirve por si hay un error lo muestre
        return render(request, 'contactoExitoso.html')
    return render(request, 'formularioContacto.html') #En caso contrario "GET", retorno el formulario contacto
