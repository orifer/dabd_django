from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /agencies/
    path('agencies/', views.agencies, name='agencies'),
    # ex: /agencies/esa/
    path('agencies/<str:agencia_id>', views.agencia, name='agencia'),

    # Delete
    path('esborrar_agencia/<str:agencia_id>', views.esborrarAgencia, name='esborrar_agencia'),
]
