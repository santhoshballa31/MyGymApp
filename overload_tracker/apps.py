from django.apps import AppConfig


class OverloadTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'overload_tracker'


    def ready(self):
        import overload_tracker.signals 
        


