from django.urls import path

from .views import Inici, LlistarAgencies, ActualitzarAgencies, CrearAgencies, EsborrarAgencies, DetallAgencia, \
    LlistarMissions, CrearMissio, DetallMissio, EsborrarMissio, ActualitzarMissio, LlistarNaus, DetallNau, CrearNau, \
    ActualitzarNau, EsborrarNau, LlistarPlataformes, DetallPlataforma, CrearPlataforma, ActualitzarPlataforma, \
    EsborrarPlataforma, LlistarAstronautes, DetallAstronauta, CrearAstronauta, ActualitzarAstronauta, \
    EsborrarAstronauta, LlistarPaisos

app_name = "spaceManager"

urlpatterns = [
    path('', Inici.as_view(), name='index'),
    path('paisos/', LlistarPaisos.as_view(), name='llistar_paisos'),

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

    path('plataformes/', LlistarPlataformes.as_view(), name='llistar_plataformes'),
    path('plataformes/<int:pk>', DetallPlataforma.as_view(), name='detall_plataforma'),
    path('crear_plataforma/', CrearPlataforma.as_view(), name='crear_plataforma'),
    path('editar_plataforma/<int:pk>', ActualitzarPlataforma.as_view(), name='editar_plataforma'),
    path('esborrar_plataforma/<int:pk>', EsborrarPlataforma.as_view(), name='esborrar_plataforma'),

    path('astronautes/', LlistarAstronautes.as_view(), name='llistar_astronautes'),
    path('astronautes/<int:pk>', DetallAstronauta.as_view(), name='detall_astronauta'),
    path('crear_astronauta/', CrearAstronauta.as_view(), name='crear_astronauta'),
    path('editar_astronauta/<int:pk>', ActualitzarAstronauta.as_view(), name='editar_astronauta'),
    path('esborrar_astronauta/<int:pk>', EsborrarAstronauta.as_view(), name='esborrar_astronauta'),
]
