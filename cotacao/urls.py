from django.urls import path
from . import views

app_name = 'cotacao'

urlpatterns = [
    path('', views.home, name='home'),
    path('sucesso', views.sucesso, name='sucesso'),
    path('erro', views.erro, name='erro')
]