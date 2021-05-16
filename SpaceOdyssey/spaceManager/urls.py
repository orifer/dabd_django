from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /agencies/
    path('agencies/', views.agencies, name='detail'),
    # ex: /agencies/esa/
    path('agencies/<str:agencia_id>', views.agencia, name='agencia'),
]
