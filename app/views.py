from django.shortcuts import render
from django.views.generic import TemplateView, FormView
import csv
from .forms import FormCSV
from .utils import guardar_csv
# Create your views here.

class Index(FormView):
    template_name = 'index.html'
    form_class = FormCSV
    success_url = 'index'
    
    def form_valid(self, form):
        archivo_csv = form.cleaned_data['archivo_csv']
        ruta_archivo = guardar_csv(archivo_csv)
        # Realiza otras acciones necesarias después de guardar el archivo
        return super().form_valid(form)
    
    # def get(self, request):
    #     # Ruta del archivo CSV
    #     csv_file = "/ruta/al/archivo.csv"

    #     # Diccionario para almacenar los datos
    #     data_dict = {}

    #     # Leer el archivo CSV y convertirlo en un diccionario
    #     with open(csv_file, "r") as file:
    #         reader = csv.DictReader(file)
    #         for row in reader:
    #             data_dict[row['clave']] = row['valor']

    #     # Devolver el diccionario como una respuesta HTTP
        
        
        """
        GUARDAR
        import os
from django.conf import settings
from django.core.files.storage import default_storage

def guardar_csv(file):
    filename = file.name
    unique_filename = os.path.join(settings.STATIC_ROOT, 'uploads', filename)
    with default_storage.open(unique_filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return unique_filename


VIEW
from django.views.generic.edit import FormView
from .forms import MiFormulario
from .utils import guardar_csv

class CargarCSVView(FormView):
    template_name = 'cargar_csv.html'
    form_class = MiFormulario
    success_url = '/exito/'

    def form_valid(self, form):
        archivo_csv = form.cleaned_data['archivo_csv']
        ruta_archivo = guardar_csv(archivo_csv)
        # Realiza otras acciones necesarias después de guardar el archivo
        return super().form_valid(form)

    """