from django.conf import settings

def media_url(request):
    return {'IMAGES_URL': settings.FILE_SERVER}