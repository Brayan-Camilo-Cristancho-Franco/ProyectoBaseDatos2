from django import forms

class FormCSV(forms.Form):
    archivo_csv = forms.FileField(
        label = "",
        widget = forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id':"formFile"})
        )

    def clean_archivo_csv(self):
        archivo = self.cleaned_data.get('archivo_csv')
        if archivo:
            if not archivo.name.endswith('.csv'):
                raise forms.ValidationError('El archivo debe ser de formato CSV.')
        return archivo
