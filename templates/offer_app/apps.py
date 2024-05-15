from django.apps import AppConfig


class OfferAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'offer_app'

    def ready(self):
        import offer_app.signals