# Django
from django.shortcuts import render

# Create your views here.
def formularioContacto(request):
    return render(request=request, template_name="formularioContacto.html")