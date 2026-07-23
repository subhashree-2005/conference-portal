from .models import WebsiteSettings

def conference_settings(request):
    settings = WebsiteSettings.objects.first()

    return {
        "settings": settings
    }