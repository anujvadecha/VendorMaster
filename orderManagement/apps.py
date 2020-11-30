from django.apps import AppConfig

class OrdermanagementConfig(AppConfig):
    name = 'orderManagement'
    def ready(self):
        import orderManagement.signals
