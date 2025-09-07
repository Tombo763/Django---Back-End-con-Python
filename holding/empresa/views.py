from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html', {})

def empresa(request):
    return render(request, 'empresa.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombreAlumno")
        apellido_p = request.POST.get("apellidoPaterno")
        apellido_m = request.POST.get("apellidoMaterno")
        rut = request.POST.get("rutAlumno")
        fecha_nac = request.POST.get("fechaDeNacimiento")


        # Ejemplo: guardar en un archivo
        archivo_nombre = f"{nombre}_{apellido_p}.txt"
        with open(archivo_nombre, "w") as f:
            f.write(f"Nombre: {nombre}\n")
            f.write(f"Apellido Paterno: {apellido_p}\n")
            f.write(f"Apellido Materno: {apellido_m}\n")
            f.write(f"RUT: {rut}\n")
            f.write(f"Fecha de nacimiento: {fecha_nac}\n")
        return HttpResponse(f"Formulario recibido de: {nombre} {apellido_p} {apellido_m}")

    return render(request, 'formulario.html', {})

def mvc(request):
    return render(request, 'mvc.html', {})
