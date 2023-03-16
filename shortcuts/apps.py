from django.apps import AppConfig


class ShortcutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shortcuts'

    def ready(self):
        # import signal handlers
        import shortcuts.signals
