from django.apps import AppConfig


class ExtracaoConfig(AppConfig):
    name = 'extracao'


    def ready(self):
        import extracao.signals