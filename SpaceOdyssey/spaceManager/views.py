from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Agencia


def index(request):
    return render(request, 'spaceManager/index.html')


def agencies(request):
    # Obtenir agencies de la base de dades
    agencies = Agencia.objects.all()

    # Crear paginacio per mostrar comodament
    agencia_paginator = Paginator(agencies, 12)
    num_pagina = request.GET.get('page')
    pagina = agencia_paginator.get_page(num_pagina)

    # context = {'agencies': agencies}
    context = {'pagina': pagina}
    return render(request, 'spaceManager/agencies.html', context)


def agencia(request, agencia_id):
    try:
        agencia = Agencia.objects.get(pk=agencia_id)
    except Agencia.DoesNotExist:
        raise Http404("Aquesta agencia no existeix")
    return render(request, 'spaceManager/agencia.html', {'agencia_id': agencia_id})


def esborrarAgencia(request, agencia_id):
    agencia = Agencia.objects.get(pk=agencia_id)
    if request.method == "POST":
        agencia.delete()
        return redirect('/agencies')

    context = {'agencia': agencia}
    return render(request, 'spaceManager/delete.html', context)
