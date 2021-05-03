from django.apps import AppConfig


class PawapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pawapi'

    def ready(self):
        import pawapi.signals
