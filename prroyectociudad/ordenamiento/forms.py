from django.forms import ModelForm
from django import forms

from ordenamiento.models import Parroquia, \
        Barrio


class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia 
        fields = ['nombre', 'tipo_parroquia'] 


class BarrioForm(ModelForm): 
    class Meta:
        model = Barrio 
        fields = ['nombre', 'numero_vivienda', 'parque', 'numero_edificio', 'parroquia'] 


class ParroquiaBarrioForm(ModelForm): 
    # *args: tupla
    def __init__(self, parroquia, *args, **kwargs):
        super(ParroquiaBarrioForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)
    
    class Meta:
        model = Barrio 
        fields = ['nombre', 'numero_vivienda', 'parque', 'numero_edificio', 'parroquia'] 
