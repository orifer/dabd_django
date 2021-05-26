from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView

from .models import Agencia
from .forms import AgenciaForm


class Inici(View):
    def get(self, request, *args, **kwargs):
        context = {'nbar': 'inici'}
        return render(request, 'spaceManager/inici.html', context)


class LlistarAgencies(View):
    model = Agencia
    template_name = 'spaceManager/agencia/llistat_agencies.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        # Paginacio
        agencia_paginator = Paginator(self.get_queryset(), 12)
        num_pagina = self.request.GET.get('page')
        pagina = agencia_paginator.get_page(num_pagina)

        context = {}
        context['pagina'] = pagina
        context['nbar'] = 'agencies'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class ActualitzarAgencies(UpdateView):
    model = Agencia
    form_class = AgenciaForm
    template_name = 'spaceManager/agencia/new_edit_agencia.html'
    success_url = reverse_lazy('spaceManager:llistar_agencies')


# Obtenir una agencia
def agencia(request, id):
    try:
        agencia = Agencia.objects.get(pk=id)
    except Agencia.DoesNotExist:
        raise Http404("Aquesta agencia no existeix")
    return render(request, 'spaceManager/agencia/detall_agencia.html', {'agencia_id': id})


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
    return render(request, 'spaceManager/agencia/new_edit_agencia.html', context)
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
    return render(request, 'spaceManager/agencia/crear.html', context)


# Esborrar una agencia
def esborrarAgencia(request, id):
    print("esborrarAgencia")
    agencia = Agencia.objects.get(pk=id)
    if request.method == "POST":
        agencia.delete()
        return redirect('/agencies')

    context = {'agencia': agencia}
    return render(request, 'spaceManager/agencia/esborrar_agencia.html', context)
