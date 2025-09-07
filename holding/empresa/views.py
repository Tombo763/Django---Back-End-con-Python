from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html', {})

def empresa(request):
    return render(request, 'empresa.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def formulario(request):
    return render(request, 'formulario.html', {})

def mvc(request):
    return render(request, 'mvc.html', {})
