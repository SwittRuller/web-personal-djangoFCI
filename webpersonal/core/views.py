from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .models import Refrigeradora, Microonda, Lavadora, Televisor, Licuadora, Cocina, Contacto
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

def principal(request):
    refrigeradoras = Refrigeradora.objects.all().order_by('-created')[:1]
    microondas = Microonda.objects.all().order_by('-created')[:1]
    lavadoras= Lavadora.objects.all().order_by('-created')[:1]
    televisors = Televisor.objects.all().order_by('-created')[:1]
    licuadoras = Licuadora.objects.all().order_by('-created')[:1]
    cocinas= Cocina.objects.all().order_by('-created')[:1]

    context = {
        'refrigeradoras': refrigeradoras,
        'microondas': microondas,
        'lavadoras': lavadoras,
        'televisors': televisors,
        'licuadoras': licuadoras,
        'cocinas': cocinas,
    }

    return render(request, "core/principal.html", context)

def nosotros(request):
    return render(request, "core/nosotros.html")

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        producto = request.POST.get('producto')
        comentario = request.POST.get('comentario')

        Contacto.objects.create(
            nombre=nombre,
            correo=correo,
            producto=producto,
            comentario=comentario
        )

        messages.success(request, '¡Gracias por tu mensaje! Te contactaremos pronto.')
        return redirect('contacto')

    return render(request, "core/contacto.html")

def productos(request):
    refrigeradoras = Refrigeradora.objects.all()
    microondas = Microonda.objects.all()
    lavadoras = Lavadora.objects.all()
    televisors = Televisor.objects.all()
    licuadoras = Licuadora.objects.all()
    cocinas = Cocina.objects.all()

    productos = {
        'refrigeradoras': refrigeradoras,
        'microondas': microondas,
        'lavadoras': lavadoras,
        'televisors': televisors,
        'licuadoras': licuadoras,
        'cocinas': cocinas,
    }

    return render(request, "core/productos.html", productos)

def refrigeradora(request, refrigeradora_id):
    refrigeradora = get_object_or_404(Refrigeradora, pk=refrigeradora_id)
    return render(request, 'core/refrigeradora.html', {'refrigeradora': refrigeradora})

def microondas(request, microonda_id):
    microonda = get_object_or_404(Microonda, pk=microonda_id)
    return render(request, 'core/microondas.html', {'microonda': microonda})

def lavadora(request, lavadora_id):
    lavadora = get_object_or_404(Lavadora, pk=lavadora_id)
    return render(request, 'core/lavadora.html', {'lavadora': lavadora})

def televisor(request, televisor_id):
    televisor = get_object_or_404(Televisor, pk=televisor_id)
    return render(request, 'core/televisor.html', {'televisor': televisor})

def licuadora(request, licuadora_id):
    licuadora = get_object_or_404(Licuadora, pk=licuadora_id)
    return render(request, 'core/licuadora.html', {'licuadora': licuadora})

def cocina(request, cocina_id):
    cocina = get_object_or_404(Cocina, pk=cocina_id)
    return render(request, 'core/cocina.html', {'cocina': cocina})

