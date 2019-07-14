from django.urls import path
from . import views

app_name = 'extracao'

urlpatterns = [
    path('', views.extrair_rg, name='extrair')
]