from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import AspirantePerfil,EmpresaPerfil
from django.conf import settings
# from django.contrib.auth import get_user_model

# User=get_user_model()

# por defecto se crea aspirante
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_usuario_inicial(sender, instance, created, **kwargs):
    if created:
        if instance.tipo_usuario == 'Aspirante':
            perfil=AspirantePerfil.objects.create(user=instance)
        else:
            perfil=EmpresaPerfil.objects.create(user=instance)
        perfil.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if not created:
        if instance.tipo_usuario == 'Aspirante':
            #verifico si se actualizo el tipo usuario
            if not AspirantePerfil.objects.filter(user=instance):
                perfil=AspirantePerfil.objects.create(user=instance)
                perfil.save()#creo un perfil de aspirante con ese usuario
                EmpresaPerfil.objects.filter(user=instance).delete()#elimino la instancia de perfil empresa de ese usuario
        else:
            # verifico si se actualizo el tipo usuario
            if not EmpresaPerfil.objects.filter(user=instance):
                perfil=EmpresaPerfil.objects.create(user=instance)
                perfil.save()
                AspirantePerfil.objects.filter(user=instance).delete()

