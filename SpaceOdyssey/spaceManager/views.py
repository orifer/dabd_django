from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from .models import Agencia
from .forms import AgenciaForm

def index(request):
    context = {'nbar': 'inici'}
    return render(request, 'spaceManager/index.html', context)


# |============|
# |  AGENCIES  |
# |============|

# Obtenir totes les agencies
def agencies(request):
    # Obtenir agencies de la base de dades
    agencies = Agencia.objects.all()

    if request.method == "POST":
        print("agencies")

    # Crear paginacio per mostrar comodament
    agencia_paginator = Paginator(agencies, 12)
    num_pagina = request.GET.get('page')
    pagina = agencia_paginator.get_page(num_pagina)

    context = {
        'pagina': pagina,
        'nbar': 'agencies'
    }
    return render(request, 'spaceManager/agencies.html', context)

# Obtenir una agencia
def agencia(request, id):
    try:
        agencia = Agencia.objects.get(pk=id)
    except Agencia.DoesNotExist:
        raise Http404("Aquesta agencia no existeix")
    return render(request, 'spaceManager/agencia.html', {'agencia_id': id})


# Crear una agencia
def crearAgencia(request):
    print("crearAgencia")

    form = AgenciaForm()

    if request.method == "POST":
        form = AgenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/agencies')

    context = {'form': form}
    return render(request, 'spaceManager/modal.html', context)
    # return render(request, 'spaceManager/crear.html', context)


# Actualitza una agencia
def modificaAgencia(request, id):
    print("modificaAgencia")
    agencia = Agencia.objects.get(pk=id)
    form = AgenciaForm(instance=agencia)

    if request.method == "POST":
        form = AgenciaForm(request.POST, instance=agencia)
        if form.is_valid():
            form.save()
            return redirect('/agencies')

    context = {'form': form}
    return render(request, 'spaceManager/crear.html', context)


# Esborrar una agencia
def esborrarAgencia(request, id):
    print("esborrarAgencia")
    agencia = Agencia.objects.get(pk=id)
    if request.method == "POST":
        agencia.delete()
        return redirect('/agencies')

    context = {'agencia': agencia}
    return render(request, 'spaceManager/delete.html', context)
