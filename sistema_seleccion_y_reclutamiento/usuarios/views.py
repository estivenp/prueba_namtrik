from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, UpdateView
from .forms import UsuarioAnonimoModelForm, RegistroUsuarioForm
from convocatoria.models import Convocatoria
from .models import AnonimoPerfil, AspirantePerfil,Usuario
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SignupView(FormView):
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/signup.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class UsuarioAnonimoView(FormView):
    form_class = UsuarioAnonimoModelForm
    template_name = 'usuarios/usuario_anonimo.html'
    success_url = '/'

    def form_valid(self, form):
        url = self.request.get_full_path()
        aux = url.split('/')
        id_conv = aux[len(aux)-1]
        form.instance.id_convocatoria=id_conv
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class UsuarioAspiranteUpdate(UpdateView):
    model = AspirantePerfil
    template_name = 'usuarios/usuario_aspirante.html'
    success_url = '/'
    fields = ('curriculo',)

    def form_valid(self, form):
        url = self.request.get_full_path()
        aux = url.split('/')
        id_conv = aux[len(aux)-1]
        conv = Convocatoria.objects.filter(id=id_conv)[0]
        conv.aspirantes.add(form.instance)
        return super().form_valid(form)
