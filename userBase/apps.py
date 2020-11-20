from django.apps import AppConfig

class UserbaseConfig(AppConfig):
    name = 'userBase'
    def ready(self):
        import userBase.signals
