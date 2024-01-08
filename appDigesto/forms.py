from django.forms import ModelForm
from .models import Digesto
from .models import Categoria
from .models import Subcategoria

from django import forms
class DigestoForm(ModelForm):
    class Meta:
        model = Digesto
        fields = ['estado','numeroDigesto','palabrasClave','fecha_vigencia', 'descripcion','archivo','categoria','subcategoria']
        widgets = {
            'fecha_vigencia': forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super(DigestoForm, self).__init__(*args, **kwargs)
        
        # Aplicar clases de Bootstrap a campos específicos
        for field_name in ['categoria', 'subcategoria']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

        # Usar ModelChoiceField para campos ForeignKey
        self.fields['categoria'].queryset = Categoria.objects.all()  # Reemplaza 'Categoria' con el nombre real de tu modelo
        self.fields['subcategoria'].queryset = Subcategoria.objects.all()  # Reemplaza 'SubCategoria' con el nombre real de tu modelo