from django.urls import path

from .views import Inici, LlistarAgencies, ActualitzarAgencies, CrearAgencies, EsborrarAgencies, DetallAgencia, \
    LlistarMissions, CrearMissio, DetallMissio, EsborrarMissio, ActualitzarMissio, LlistarNaus, DetallNau, CrearNau, \
    ActualitzarNau, EsborrarNau

app_name = "spaceManager"

urlpatterns = [
    path('', Inici.as_view(), name='index'),

    path('agencies/', LlistarAgencies.as_view(), name='llistar_agencies'),
    path('agencies/<int:pk>', DetallAgencia.as_view(), name='detall_agencia'),
    path('crear_agencia/', CrearAgencies.as_view(), name='crear_agencia'),
    path('editar_agencia/<int:pk>', ActualitzarAgencies.as_view(), name='editar_agencia'),
    path('esborrar_agencia/<int:pk>', EsborrarAgencies.as_view(), name='esborrar_agencia'),

    path('missions/', LlistarMissions.as_view(), name='llistar_missions'),
    path('missions/<int:pk>', DetallMissio.as_view(), name='detall_missio'),
    path('crear_missio/', CrearMissio.as_view(), name='crear_missio'),
    path('editar_missio/<int:pk>', ActualitzarMissio.as_view(), name='editar_missio'),
    path('esborrar_missio/<int:pk>', EsborrarMissio.as_view(), name='esborrar_missio'),

    path('naus/', LlistarNaus.as_view(), name='llistar_naus'),
    path('naus/<int:pk>', DetallNau.as_view(), name='detall_nau'),
    path('crear_nau/', CrearNau.as_view(), name='crear_nau'),
    path('editar_nau/<int:pk>', ActualitzarNau.as_view(), name='editar_nau'),
    path('esborrar_nau/<int:pk>', EsborrarNau.as_view(), name='esborrar_nau'),
]
