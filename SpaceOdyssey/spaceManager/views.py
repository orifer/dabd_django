# https://docs.djangoproject.com/en/3.2/topics/db/queries/

from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, CreateView, DeleteView

from .models import Agencia, Missio
from .forms import AgenciaForm, AgenciaFormLectura, MissioForm, MissioFormLectura


class Inici(View):
    def get(self, request, *args, **kwargs):
        context = {'nbar': 'inici'}
        return render(request, 'spaceManager/inici.html', context)



''' AGENCIES '''

class LlistarAgencies(View):
    model = Agencia
    template_name = 'spaceManager/agencia/llistat_agencies.html'

    def get_queryset(self):
        return self.model.objects.order_by('id')

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

class DetallAgencia(UpdateView):
    model = Agencia
    form_class = AgenciaFormLectura
    template_name = 'spaceManager/agencia/detall_agencia.html'

class CrearAgencies(CreateView):
    model = Agencia
    form_class = AgenciaForm
    template_name = 'spaceManager/agencia/crear_agencia.html'
    success_url = reverse_lazy('spaceManager:llistar_agencies')

class ActualitzarAgencies(UpdateView):
    model = Agencia
    form_class = AgenciaForm
    template_name = 'spaceManager/agencia/editar_agencia.html'
    success_url = reverse_lazy('spaceManager:llistar_agencies')

class EsborrarAgencies(DeleteView):
    model = Agencia
    template_name = 'spaceManager/agencia/esborrar_agencia.html'
    success_url = reverse_lazy('spaceManager:llistar_agencies')



''' MISSIONS '''

class LlistarMissions(View):
    model = Missio
    template_name = 'spaceManager/missio/llistat_missions.html'

    def get_queryset(self):
        return self.model.objects.order_by('id')

    def get_context_data(self, **kwargs):
        # Paginacio
        paginator = Paginator(self.get_queryset(), 12)
        num_pagina = self.request.GET.get('page')
        pagina = paginator.get_page(num_pagina)

        context = {}
        context['pagina'] = pagina
        context['nbar'] = 'missions'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class DetallMissio(UpdateView):
    model = Missio
    form_class = MissioFormLectura
    template_name = 'spaceManager/agencia/detall_agencia.html'

class CrearMissio(CreateView):
    model = Missio
    form_class = MissioForm
    template_name = 'spaceManager/missio/crear_missio.html'
    success_url = reverse_lazy('spaceManager:llistar_missions')

class ActualitzarMissio(UpdateView):
    model = Missio
    form_class = MissioForm
    template_name = 'spaceManager/agencia/editar_missio.html'
    success_url = reverse_lazy('spaceManager:llistar_missions')

class EsborrarMissio(DeleteView):
    model = Missio
    template_name = 'spaceManager/agencia/esborrar_missio.html'
    success_url = reverse_lazy('spaceManager:llistar_missions')