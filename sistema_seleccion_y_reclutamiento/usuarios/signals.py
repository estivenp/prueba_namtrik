from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import AspirantePerfil,EmpresaPerfil,AnonimoPerfil
from django.conf import settings
from convocatoria.models import Convocatoria

# por defecto se crea aspirante
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_usuario_inicial(sender, instance, created, **kwargs):
    if created:
        if instance.tipo_usuario == 'Aspirante':
            perfil=AspirantePerfil.objects.create(user=instance)
        else:
            perfil=EmpresaPerfil.objects.create(user=instance)
        perfil.save()

#cuando se actualiza el tipo de usuario, se ajusta el perfil
#ejemplo si se actuliza de aspirante a empresa, se crea el prefil empresa y se elimina el perfil aspirante
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


#cuando se crea un usario anonimo, se registra en la lista de usuarios anonimos de la 
# convocatoria a la que aplico
@receiver(post_save, sender=AnonimoPerfil)
def aplicar_convocatoria_anonimo(sender, instance, created, **kwargs):
    if created:
        id_conv=instance.id_convocatoria
        convocatoria=Convocatoria.objects.filter(id=id_conv)[0]
        convocatoria.aspirantes_anonimos.add(instance)

