from django.urls import path

from . import views

urlpatterns = [

    # ex: /
    path('', views.index, name='index'),

    # |============|
    # |  AGENCIES  |
    # |============|

    # ex: /agencies/
    path('agencies/', views.agencies, name='agencies'),
    # ex: /agencies/esa/
    path('agencies/<int:id>', views.agencia, name='agencia'),
    # Crea
    path('crear_agencia/', views.crearAgencia, name='crear_agencia'),
    # Modifica
    path('modifica_agencia/<int:id>', views.modificaAgencia, name='modifica_agencia'),
    # Delete
    path('esborrar_agencia/<int:id>', views.esborrarAgencia, name='esborrar_agencia'),
]
