from django.apps import AppConfig


class SignalsConfig(AppConfig):
    name = 'signals'

    def ready(self):
        import signals.handlers # noqa