from django.shortcuts import render ,HttpResponse
from django.views.generic import TemplateView, FormView, View
import csv
from .forms import FormCSV
from .utils import guardar_csv, cargar_csv
# 
import os
from django.conf import settings
import json
from django.http import JsonResponse

# Create your views here.

class Index(FormView):
    template_name = 'index.html'
    form_class = FormCSV
    success_url = '/process-csv'
    
    def form_valid(self, form):
        archivo_csv = form.cleaned_data['archivo_csv']
        ruta_archivo = guardar_csv(archivo_csv)
        # Realiza otras acciones necesarias después de guardar el archivo
        return super().form_valid(form)

    def mostrar_csv():
        data = cargar_csv()
        print(data)
        
class ConvertirCSVView(View):
    def get(self, request):
        response = cargar_csv()
        return JsonResponse(response, safe=False)

