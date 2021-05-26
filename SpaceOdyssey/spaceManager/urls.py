from django.urls import path

from . import views
from .views import Inici, LlistarAgencies, ActualitzarAgencies

app_name = "spaceManager"

urlpatterns = [
    path('', Inici.as_view(), name='index'),
    path('agencies/', LlistarAgencies.as_view(), name='llistar_agencies'),
    path('agencies/<int:id>', views.agencia, name='agencia'),
    path('crear_agencia/', views.crearAgencia, name='crear_agencia'),
    path('editar_agencia/<int:pk>', ActualitzarAgencies.as_view(), name='editar_agencia'),
    path('esborrar_agencia/<int:id>', views.esborrarAgencia, name='esborrar_agencia'),
]
