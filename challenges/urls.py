
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index),
    path("<int:mes>", views.mes_numero),
    path("<str:mes>", views.mes, name='desafio_mes')
]
