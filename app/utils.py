import os
from django.conf import settings
from django.core.files.storage import default_storage
import csv
from django.http import JsonResponse


def guardar_csv(file):
    global filename
    filename = file.name
    unique_filename = os.path.join(settings.MEDIA_ROOT, 'files', filename)
    with default_storage.open(unique_filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return unique_filename

def cargar_csv():
    ruta_media = settings.MEDIA_ROOT
    file = "{}/files/{}".format(ruta_media,"ETL.csv") 
    #csv_file_path = os.path.join(settings.BASE_DIR, 'files', 'ETL.csv')
    json_data = []

    with open(file, 'r') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=';')
        headers = next(csv_data)  # Obtener los títulos de las columnas

        for row in csv_data:
            row_dict = {headers[0]: row[0], headers[1]: row[1], headers[2]: row[2]}  # Asignar títulos a cada columna
            json_data.append(row_dict)

        response_data = {
            'data': json_data
        }
    return response_data