from django.db import models
from usuarios.models import EmpresaPerfil,AnonimoPerfil,AspirantePerfil
from django.utils.translation import gettext_lazy as _

class Convocatoria(models.Model):
    cargo=models.CharField(max_length=100)
    descripcion=models.TextField()
    fecha_cierre=models.DateField(default=None)
    hora_cierre=models.TimeField(default=None)
    estado=models.CharField(max_length=10,choices=(('ABIERTA','ABIERTA'),('CERRADA','CERRADA'),('TERMINADA','TERMINADA'))
    ,default='ABIERTA')
    empresa=models.ForeignKey(EmpresaPerfil,on_delete=models.CASCADE)
    aspirantes=models.ManyToManyField(AspirantePerfil)
    aspirantes_anonimos=models.ManyToManyField(AnonimoPerfil)

    class Meta:
        verbose_name= _('Convocatoria')
        verbose_name_plural= _('Convocatorias')
        ordering = ['fecha_cierre','hora_cierre']

    def __str__(self):
        return self.empresa.user.username + ' - ' + self.cargo 
