from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CrearConvocatoriaModelForm
from .models import Convocatoria
from datetime import date, time, datetime
from usuarios.models import EmpresaPerfil, AspirantePerfil

@method_decorator(login_required, name='dispatch')
class CrearConvocatoriaView(FormView):
    form_class = CrearConvocatoriaModelForm
    template_name = 'convocatoria/crear_convocatoria.html'
    success_url = '/'

    def form_valid(self, form):
        empresa = EmpresaPerfil.objects.filter(user=self.request.user)[0]
        # form.instance.empresa = empresa
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('formulario: ', form)
        return super().form_invalid(form)


class ConvocatoriasView(ListView):
    model = Convocatoria
    template_name = 'convocatoria/convocatorias.html'
    # paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['fecha'] = date.today()
        return contex

@method_decorator(login_required, name='dispatch')
class MisConvocatoriasView(ListView):
    model = Convocatoria
    template_name = 'convocatoria/mis_convocatorias.html'
    # paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        datos = []
        convocatorias = Convocatoria.objects.filter(
            empresa=EmpresaPerfil.objects.filter(user=self.request.user)[0])
        for convocatoria in convocatorias:
            object_list = {
                'id': convocatoria.id,
                'cargo': convocatoria.cargo,
                'fecha_cierre': convocatoria.fecha_cierre,
                'hora_cierre': convocatoria.hora_cierre,
                'numero_aspirantes': convocatoria.aspirantes.count()+convocatoria.aspirantes_anonimos.count()
            }
            datos.append(object_list)

        context['object_list'] = datos
        context['fecha'] = date.today()
        return context

@method_decorator(login_required, name='dispatch')
class MisConvocatoriasAspiranteView(ListView):
    model = Convocatoria
    template_name = 'convocatoria/convocatorias_aspirante.html'
    # paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        datos = []
        convocatorias = AspirantePerfil.objects.get(
            user_id=self.request.user.id).convocatoria_set.all()
        for convocatoria in convocatorias:
            object_list = {
                'id': convocatoria.id,
                'cargo': convocatoria.cargo,
                'fecha_cierre': convocatoria.fecha_cierre,
                'hora_cierre': convocatoria.hora_cierre,
                'estado': convocatoria.estado
            }
            datos.append(object_list)

        context['object_list'] = datos
        context['fecha'] = date.today()
        return context

# vistas basadas en clases

@method_decorator(login_required, name='dispatch')
class DetalleConvocatoriaView(ListView):
    model = Convocatoria
    template_name = 'convocatoria/detalle_convocatoria.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        url = self.request.get_full_path()
        aux = url.split('/')
        id_conv = aux[len(aux)-1]
        convocatoria=Convocatoria.objects.filter(id=id_conv)[0]
        contexto = {
            'convocatoria':convocatoria,
            'aspirantes': convocatoria.aspirantes.all(),
            'aspirantes_anonimos': convocatoria.aspirantes_anonimos.all()
        }
        return contexto