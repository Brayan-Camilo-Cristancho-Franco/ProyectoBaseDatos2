import pandas as pd
from django.shortcuts import render
from django.db import connection
from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView
from .models import *
from .forms import FormCSV

class CSVImporterView(FormView):
    template_name = 'index.html'  # Nombre de la plantilla que se utilizará para renderizar la vista
    form_class = FormCSV  # Clase del formulario que se utilizará para procesar los datos de entrada
    success_url = '/table'  # URL de redirección después de que el formulario se haya procesado correctamente

    def form_valid(self, form):
        archivo_csv = form.cleaned_data['archivo_csv']  # Obtener el archivo CSV enviado en el formulario
        
        tipos_de_datos_mysql = {
            'ID_Empresa': 'INT',
            'Nit_Empresa': 'VARCHAR(20)',
            'Nombre_Empresa': 'VARCHAR(50)',
            'Direccion_Empresa': 'VARCHAR(100)',
            'Sector_Empresa': 'VARCHAR(50)',
            'Correo_Empresa': 'VARCHAR(50)',
            'ID_Proyecto': 'INT',
            'Nombre_Proyecto': 'VARCHAR(50)',
            'Descripcion_Proyecto': 'VARCHAR(200)',
            'Fecha_Inicio_Proyecto': 'DATE',
            'Fecha_Finalizacion_Proyecto': 'DATE',
            'Id_Empresa_Proyecto': 'INT',
            'Estado_Proyecto': 'BOOL',
            'ID_M_Pago': 'INT',
            'Nombre_M_Pago': 'VARCHAR(50)',
            'Descripcion_M_Pago': 'VARCHAR(100)',
            'Estado_M_Pago': 'BOOL',
            'ID_Factura': 'INT',
            'Fecha_Factura': 'DATE',
            'Valor_Factura': 'FLOAT',
            'Id_M_Pago_Factura': 'INT',
            'ID_T_Servicio': 'INT',
            'Nombre_T_Servicio': 'VARCHAR(50)',
            'Descripcion_T_Servicio': 'VARCHAR(100)',
            'Estado_T_Servicio': 'BOOL',
            'ID_Consultoria': 'INT',
            'Id_Factura_Consultoria': 'INT',
            'Id_T_Servicio_Consultoria': 'INT',
            'Estado_Consultoria': 'BOOL',
            'ID_CONS_EMP': 'INT',
            'id_Consultoria_CONS_EMP': 'INT',
            'id_Empresa_CONS_EMP': 'INT',
            'ID_Consultor': 'INT',
            'Nombre_Consultor': 'VARCHAR(100)',
            'Telefono_Consultor': 'VARCHAR(10)',
            'Correo_Consultor': 'VARCHAR(50)',
            'Area_Especializacion_Consultor': 'VARCHAR(50)',
            'ESTADO_Consultor': 'BOOL',
            'ID_CONS_CONS': 'INT',
            'Id_Consultoria_CONS_CONS': 'INT',
            'Id_Consultor_CONS_CONS': 'INT'
        }

        # Leer el archivo CSV con pandas y almacenar los datos en un DataFrame
        df = pd.read_csv(archivo_csv)

        # Nombre de la tabla temporal en la base de datos
        nombre_tabla_temporal = "TablaTemporal"

        # Crear la tabla temporal si no existe utilizando un cursor de la conexión a la base de datos
        with connection.cursor() as cursor:
            create_table_query = f"CREATE TEMPORARY TABLE IF NOT EXISTS {nombre_tabla_temporal} ("
            create_table_query += ", ".join([f"{column} {tipos_de_datos_mysql[column]}" for column in df.columns])
            create_table_query += ")"
            cursor.execute(create_table_query)
            try:
                # Insertar los datos del DataFrame en la tabla temporal
                for index, row in df.iterrows():
                    insert_query = f"INSERT INTO {nombre_tabla_temporal} ("
                    insert_query += ", ".join(row.index)
                    insert_query += ") VALUES ("
                    insert_query += ", ".join([f"%s"] * len(row))
                    insert_query += ")"
                    cursor.execute(insert_query, tuple(row))

                # Llamar al procedimiento almacenado "AgregarEmpresa" en la base de datos
                cursor.callproc('AgregarEmpresa')
                cursor.callproc('AgregarProyecto')
                cursor.callproc('AgregarMetodoPago')
                cursor.callproc('AgregarFactura')
                cursor.callproc('AgregarTipoServicio')
                cursor.callproc('AgregarConsultoria')
                cursor.callproc('AgregarConsEmp')
                cursor.callproc('AgregarConsultor')
                cursor.callproc('AgregarConsCons')

                # Comprobar si se creó la tabla temporal y mostrar los registros
                cursor.execute(f"SELECT * FROM {nombre_tabla_temporal}")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            finally:
                # Eliminar tabla temporal
                print("TABLA ELIMINADA")
                cursor.execute(f"DROP TABLE IF EXISTS {nombre_tabla_temporal}")

        return super().form_valid(form)  # Llamar al método form_valid() de la clase padre para finalizar el procesamiento del formulario


class TableView(TemplateView):
    template_name = 'tables.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresas'] = Empresa.objects.all()
        context['proyectos'] = Proyecto.objects.all()
        context['metodos_pago'] = MetodoPago.objects.all()
        context['facturas'] = Factura.objects.all()
        context['tipos_servicio'] = TipoServicio.objects.all()
        context['consultorias'] = Consultoria.objects.all()
        context['cons_emps'] = ConsEmp.objects.all()
        context['consultores'] = Consultor.objects.all()
        context['cons_conses'] = ConsCons.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        if 'borrar_datos' in request.POST:
            with connection.cursor() as cursor:
                    cursor.callproc('BorrarDatosTablas')

        return render(request, self.template_name, self.get_context_data())
    