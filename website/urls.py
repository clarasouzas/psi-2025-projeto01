from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('elenco/<int:id_post>/',views.elenco, name="elenco"),
    path('elenco/', views.elenco_list, name='elenco_list'),
    path('sobre/',views.sobre, name="sobre"),


]
