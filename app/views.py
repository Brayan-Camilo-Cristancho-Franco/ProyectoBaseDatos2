from django.shortcuts import render ,HttpResponse
from django.views.generic import TemplateView, FormView, View
import csv
from .forms import FormCSV
from .utils import guardar_csv, cargar_csv
from .models import TablaInicial
# 
import os
from django.conf import settings
import json
from django.http import JsonResponse
import pandas as pd
from django.db import connection


# Create your views here.

# class Index(FormView):
#     template_name = 'index.html'
#     form_class = FormCSV
#     success_url = '/process-csv'
    
#     def form_valid(self, form):
#         archivo_csv = form.cleaned_data['archivo_csv']
#         ruta_archivo = guardar_csv(archivo_csv)
#         # Realiza otras acciones necesarias después de guardar el archivo
#         return super().form_valid(form)

#     def mostrar_csv():
#         data = cargar_csv()
#         print(data)
    
#     def importar_datos(self):
#         with open(self.archivo, 'r') as csv_file:
#             reader = csv.reader(csv_file)
#             for row in reader:
#                 # Inserta los datos en tu modelo temporal
#                 tabla_inicial = TablaInicial(CODIGO_FACTURA=row[0], PRECIO=row[1], NOMBRE=row[2])
#                 tabla_inicial.save()

    
class ConvertirCSVView(View):
    def get(self, request):
        response = cargar_csv()
        
        return JsonResponse(response, safe=False)
    
class CSVImporterView(FormView):
    template_name = 'index.html'
    form_class = FormCSV
    success_url = '/import-csv'

    def form_valid(self, form):
        archivo_csv = form.cleaned_data['archivo_csv']

        # Leer el archivo CSV con pandas
        df = pd.read_csv(archivo_csv)
        print(df)
        # Insertar los datos en la tabla temporal utilizando el cursor de Django
        with connection.cursor() as cursor:
            # Nombre de la tabla temporal en tu base de datos
            nombre_tabla_temporal = "TablaTemporalPrueba2"

            # Crear la tabla temporal si no existe
            cursor.execute(f"CREATE TEMPORARY TABLE IF NOT EXISTS {nombre_tabla_temporal} (CODIGO_FACTURA INT, PRECIO INT, NOMBRE VARCHAR(255))")

            # Insertar los datos en la tabla temporal
            for index, row in df.iterrows():
                cursor.execute(f"INSERT INTO {nombre_tabla_temporal} (CODIGO_FACTURA, PRECIO, NOMBRE) VALUES (%s, %s, %s)",
                               [row['CODIGO_FACTURA'], row['PRECIO'], row['NOMBRE']])
            
            cursor.callproc('AgregarDatosDesdeTemporal')
            # Insertar los datos de la tabla temporal en la tabla Prueba
            # cursor.execute("""
            #     INSERT INTO Prueba (CODIGO_FACTURA, PRECIO, NOMBRE)
            #     SELECT CODIGO_FACTURA, PRECIO, NOMBRE
            #     FROM TablaTemporalPrueba2
            # """)
            #COMPRUEBA SI SE CREO LA TABLA TEMPORAL    
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM TablaTemporalPrueba2")
                rows = cursor.fetchall()

                for row in rows:
                    print(row)
        return super().form_valid(form)



""""

def importar_csv(request):
    if request.method == 'POST' and request.FILES['archivo_csv']:
        archivo_csv = request.FILES['archivo_csv']

        # Lee el archivo CSV y realiza la inserción en la tabla temporal
        reader = csv.reader(archivo_csv)
        for row in reader:
            # Inserta los datos en tu modelo temporal
            tu_modelo_temporal = TuModeloTemporal(campo1=row[0], campo2=row[1], ...)
            tu_modelo_temporal.save()

        return HttpResponse('CSV importado exitosamente')
    else:
        return render(request, 'importar_csv.html')
        
        
def importar_csv(request):
    if request.method == 'POST' and request.FILES['archivo_csv']:
        archivo_csv = request.FILES['archivo_csv']

        # Lee el archivo CSV utilizando pandas
        df = pd.read_csv(archivo_csv)

        # Itera sobre cada fila del DataFrame y realiza la inserción en la tabla temporal
        for _, row in df.iterrows():
            tu_modelo_temporal = TuModeloTemporal(campo1=row['campo1'], campo2=row['campo2'], ...)
            tu_modelo_temporal.save()

        return HttpResponse('CSV importado exitosamente')
    else:
        return render(request, 'importar_csv.html')        
        
        
def importar_csv(request):
    if request.method == 'POST' and request.FILES['archivo_csv']:
        archivo_csv = request.FILES['archivo_csv']

        # Crea una instancia del ImportadorCSV y realiza la importación
        importador = ImportadorCSV(archivo_csv)
        importador.importar_datos()

        return HttpResponse('CSV importado exitosamente')
    else:
        return render(request, 'importar_csv.html')
        
        ------------------------------------------
        import pandas as pd
from django.db import connection

class CSVImporter:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def import_data(self):
        # Leer el archivo CSV con pandas
        df = pd.read_csv(self.csv_file)

        # Insertar los datos en la tabla temporal utilizando el cursor de Django
        with connection.cursor() as cursor:
            # Nombre de la tabla temporal en tu base de datos
            nombre_tabla_temporal = "TablaTemporal"

            # Crear la tabla temporal si no existe
            cursor.execute(f"CREATE TEMPORARY TABLE IF NOT EXISTS {nombre_tabla_temporal} (campo1 VARCHAR(255), campo2 INT)")

            # Insertar los datos en la tabla temporal
            for index, row in df.iterrows():
                cursor.execute(f"INSERT INTO {nombre_tabla_temporal} (campo1, campo2) VALUES (%s, %s)", [row['campo1'], row['campo2']])

"""""