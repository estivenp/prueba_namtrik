from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Convocatoria
from usuarios.models import EmpresaPerfil
from datetime import date


class CrearConvocatoriaModelForm(forms.ModelForm):

    class Meta:
        model = Convocatoria
        fields = ('cargo', 'descripcion', 'fecha_cierre','hora_cierre', 'estado')
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Cargo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control form-control-user', 'rows': 3, 'placeholder': 'Descripcion'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control form-control-user',
                                                   'placeholder': 'Fecha de cierre', 'type': 'date', 'min': date.today()}),
            'hora_cierre': forms.TimeInput(attrs={'class': 'form-control form-control-user',
                                                  'placeholder': 'Hora de cierre', 'type': 'time'}),
            'estado': forms.Select(attrs={'class': 'form-control '})
        }

    def save(self, commit=True):
        return super().save(commit=commit)

class CrearConvocatoriaApiModelForm(forms.ModelForm):

    class Meta:
        model = Convocatoria
        fields = ('empresa','cargo', 'descripcion', 'fecha_cierre','hora_cierre', 'estado')
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Cargo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control form-control-user', 'rows': 3, 'placeholder': 'Descripcion'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control form-control-user',
                                                   'placeholder': 'Fecha de cierre', 'type': 'date', 'min': date.today()}),
            'hora_cierre': forms.TimeInput(attrs={'class': 'form-control form-control-user',
                                                  'placeholder': 'Hora de cierre', 'type': 'time'}),
            'estado': forms.Select(attrs={'class': 'form-control '})
        }

    def save(self, commit=True):
        return super().save(commit=commit)
