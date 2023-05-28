import os
from django.conf import settings
from django.core.files.storage import default_storage

def guardar_csv(file):
    filename = file.name
    unique_filename = os.path.join(settings.MEDIA_ROOT, 'files', filename)
    with default_storage.open(unique_filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return unique_filename
