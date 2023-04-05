from django.apps import AppConfig



class VendorBaseConfig(AppConfig):
    name = 'vendorbase'
    def ready(self):
        import vendorbase.signals

