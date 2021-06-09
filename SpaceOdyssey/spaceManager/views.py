# https://docs.djangoproject.com/en/3.2/topics/db/queries/

from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, CreateView, DeleteView

from .models import Agencia, Missio, Nau, Plataforma, Astronauta, Pais
from .forms import AgenciaForm, AgenciaFormLectura, MissioForm, MissioFormLectura, NauFormLectura, NauForm, \
    PlataformaForm, PlataformaFormLectura, AstronautaForm, AstronautaFormLectura



''' INICI '''

class Inici(View):
    def get(self, request, *args, **kwargs):
        context = {'nbar': 'inici'}
        return render(request, 'spaceManager/inici.html', context)



''' PAïSOS '''

class LlistarPaisos(View):
    model = Pais
    template_name = 'spaceManager/pais/llistat_paisos.html'

    def get_queryset(self):
        return self.model.objects.order_by('nom')

    def get_context_data(self, **kwargs):
        # Paginacio
        agencia_paginator = Paginator(self.get_queryset(), 12)
        num_pagina = self.request.GET.get('page')
        pagina = agencia_paginator.get_page(num_pagina)

        context = {}
        context['pagina'] = pagina
        context['nbar'] = 'paisos'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())



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
    template_name = 'spaceManager/missio/detall_missio.html'

class CrearMissio(CreateView):
    model = Missio
    form_class = MissioForm
    template_name = 'spaceManager/missio/crear_missio.html'
    success_url = reverse_lazy('spaceManager:llistar_missions')

class ActualitzarMissio(UpdateView):
    model = Missio
    form_class = MissioForm
    template_name = 'spaceManager/missio/editar_missio.html'
    success_url = reverse_lazy('spaceManager:llistar_missions')

class EsborrarMissio(DeleteView):
    model = Missio
    template_name = 'spaceManager/missio/esborrar_missio.html'
    success_url = reverse_lazy('spaceManager:llistar_missions')



''' NAUS '''

class LlistarNaus(View):
    model = Nau
    template_name = 'spaceManager/nau/llistat_naus.html'

    def get_queryset(self):
        return self.model.objects.order_by('id')

    def get_context_data(self, **kwargs):
        # Paginacio
        paginator = Paginator(self.get_queryset(), 12)
        num_pagina = self.request.GET.get('page')
        pagina = paginator.get_page(num_pagina)

        context = {}
        context['pagina'] = pagina
        context['nbar'] = 'naus'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class DetallNau(UpdateView):
    model = Nau
    form_class = NauFormLectura
    template_name = 'spaceManager/nau/detall_nau.html'

class CrearNau(CreateView):
    model = Nau
    form_class = NauForm
    template_name = 'spaceManager/nau/crear_nau.html'
    success_url = reverse_lazy('spaceManager:llistar_naus')

class ActualitzarNau(UpdateView):
    model = Nau
    form_class = NauForm
    template_name = 'spaceManager/nau/editar_nau.html'
    success_url = reverse_lazy('spaceManager:llistar_naus')

class EsborrarNau(DeleteView):
    model = Nau
    template_name = 'spaceManager/nau/esborrar_nau.html'
    success_url = reverse_lazy('spaceManager:llistar_naus')



''' PLATAFORMES '''

class LlistarPlataformes(View):
    model = Plataforma
    template_name = 'spaceManager/plataforma/llistat_plataformes.html'

    def get_queryset(self):
        return self.model.objects.order_by('id')

    def get_context_data(self, **kwargs):
        # Paginacio
        paginator = Paginator(self.get_queryset(), 12)
        num_pagina = self.request.GET.get('page')
        pagina = paginator.get_page(num_pagina)

        context = {}
        context['pagina'] = pagina
        context['nbar'] = 'plataformes'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class DetallPlataforma(UpdateView):
    model = Plataforma
    form_class = PlataformaFormLectura
    template_name = 'spaceManager/plataforma/detall_plataforma.html'

class CrearPlataforma(CreateView):
    model = Plataforma
    form_class = PlataformaForm
    template_name = 'spaceManager/plataforma/crear_plataforma.html'
    success_url = reverse_lazy('spaceManager:llistar_plataformes')

class ActualitzarPlataforma(UpdateView):
    model = Plataforma
    form_class = PlataformaForm
    template_name = 'spaceManager/plataforma/editar_plataforma.html'
    success_url = reverse_lazy('spaceManager:llistar_plataformes')

class EsborrarPlataforma(DeleteView):
    model = Plataforma
    template_name = 'spaceManager/plataforma/esborrar_plataforma.html'
    success_url = reverse_lazy('spaceManager:llistar_plataformes')



''' ASTRONAUTES '''

class LlistarAstronautes(View):
    model = Astronauta
    template_name = 'spaceManager/astronauta/llistat_astronautes.html'

    def get_queryset(self):
        return self.model.objects.order_by('id')

    def get_context_data(self, **kwargs):
        # Paginacio
        paginator = Paginator(self.get_queryset(), 12)
        num_pagina = self.request.GET.get('page')
        pagina = paginator.get_page(num_pagina)

        context = {}
        context['pagina'] = pagina
        context['nbar'] = 'astronautes'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class DetallAstronauta(UpdateView):
    model = Astronauta
    form_class = AstronautaFormLectura
    template_name = 'spaceManager/astronauta/detall_astronauta.html'

class CrearAstronauta(CreateView):
    model = Astronauta
    form_class = AstronautaForm
    template_name = 'spaceManager/astronauta/crear_astronauta.html'
    success_url = reverse_lazy('spaceManager:llistar_astronautes')

class ActualitzarAstronauta(UpdateView):
    model = Astronauta
    form_class = AstronautaForm
    template_name = 'spaceManager/astronauta/editar_astronauta.html'
    success_url = reverse_lazy('spaceManager:llistar_astronautes')

class EsborrarAstronauta(DeleteView):
    model = Astronauta
    template_name = 'spaceManager/astronauta/esborrar_astronauta.html'
    success_url = reverse_lazy('spaceManager:llistar_astronautes')

