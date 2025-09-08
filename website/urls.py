from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('elenco/', views.elenco, name='elenco'),
    path('ator/<int:id_ator>/', views.ator, name='ator'),
]