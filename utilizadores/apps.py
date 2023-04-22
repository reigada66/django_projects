from django.apps import AppConfig


class UtilizadoresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "utilizadores"


    def ready(self):
        import utilizadores.signals