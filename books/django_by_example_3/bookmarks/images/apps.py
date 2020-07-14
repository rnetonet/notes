from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

    def ready(self) -> None:
        from . import signals
