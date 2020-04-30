from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import validate_file_extension,validate_file_size


# usuario
class Usuario(AbstractUser):
    tipo_usuario = models.CharField(max_length=10, choices=(
        ('Aspirante', 'Aspirante'), ('Empresa', 'Empresa')), default='Aspirante')
    email = models.EmailField(unique=True, max_length=200)

    # USERNAME_FIELD define lo que Django utilizará para reconocer al usuario al momento de la autentificación
    USERNAME_FIELD = 'email'
    # correo y contraseña son requeridos por defecto
    REQUIRED_FIELDS = ['username']

    def get_aspirante_profile(self):
        aspirante_perfil = None
        if hasattr(self, 'aspiranteperfil'):
            aspirante_perfil = self.aspiranteperfil
        return aspirante_perfil

    def get_empresa_profile(self):
        empresa_perfil = None
        if hasattr(self, 'empresaperfil'):
            empresa_perfil = self.empresaperfil
        return empresa_perfil


# Perfiles, (empresa,aspirante y anonimo), el administrador es el superadmin y no es necesario crear un perfil

# perfil para aspirante ya sea logeado o anonimo


class AspirantePerfil(models.Model):
    user = models.OneToOneField(
        Usuario, primary_key=True, on_delete=models.CASCADE)
    curriculo = models.FileField(upload_to='curriculos', blank=True, validators=[
                                validate_file_extension,validate_file_size])

    def __str__(self):
        return self.user.username

# perfil para empresa


class EmpresaPerfil(models.Model):
    user = models.OneToOneField(
        Usuario, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# perfil para usuario anonimo


class AnonimoPerfil(models.Model):
    nombre_completo = models.CharField(max_length=120, null=False)
    curriculo = models.FileField(upload_to='curriculos_anonimos', validators=[
                                validate_file_extension,validate_file_size])

    def __str__(self):
        return self.nombre_completo
