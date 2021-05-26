from django.urls import path

from .views import Inici, LlistarAgencies, ActualitzarAgencies, CrearAgencies, EsborrarAgencies, DetallAgencia

app_name = "spaceManager"

urlpatterns = [
    path('', Inici.as_view(), name='index'),
    path('agencies/', LlistarAgencies.as_view(), name='llistar_agencies'),
    path('agencies/<int:pk>', DetallAgencia.as_view(), name='detall_agencia'),
    path('crear_agencia/', CrearAgencies.as_view(), name='crear_agencia'),
    path('editar_agencia/<int:pk>', ActualitzarAgencies.as_view(), name='editar_agencia'),
    path('esborrar_agencia/<int:pk>', EsborrarAgencies.as_view(), name='esborrar_agencia'),
]
