from django.apps import AppConfig


class EvaluatehubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EvaluateHub'

    def ready(self):
        import EvaluateHub.signals