from django.url import path
from . import views

app_name = 'extracao'

urlpatterns = [
    path('', views.extrair, name='extrair')
]