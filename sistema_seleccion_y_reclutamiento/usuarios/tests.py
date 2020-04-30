from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import AspirantePerfil,EmpresaPerfil,AnonimoPerfil
from convocatoria.models import Convocatoria
from django.core.exceptions import ObjectDoesNotExist

User=get_user_model()

class RegistroUsuarioTestCase(TestCase):
    
    def test_registro_aspirante(self):
        #al crear un usuario por defecto se crea como tipo aspirante, se crea un perfil de usuario
        # con una instancia del usuario creado
        user = User.objects.create_user(email='user@test.com', username='testuser', password='abc123')
        user.save()
        #comprobamos que exista un perfil aspirante con el usuario que se acaba de crear
        self.assertTrue(AspirantePerfil.objects.get(user=user)) 
    
    def test_registro_empresa(self):
        #se registrara un usuario ingresandole el tipo empresa
        user = User.objects.create_user(email='user@test.com', username='testuser', password='abc123',tipo_usuario="Empresa")
        user.save()
        #comprobamos que exista un perfil empresa con el usuario que se acaba de crear
        self.assertTrue(EmpresaPerfil.objects.get(user=user))

class ActualizacionTipoTestCase(TestCase):
    
    def test_actualizacion_aspirante_a_empresa(self):
        #al crear un usuario por defecto se crea como tipo aspirante, se crea un perfil de usuario
        # con una instancia del usuario creado
        user = User.objects.create_user(email='user@test.com', username='testuser', password='abc123')
        user.save()
        #comprobamos que exista un perfil aspirante con el usuario que se acaba de crear
        self.assertTrue(AspirantePerfil.objects.get(user=user)) 
        #se actualiza el tipo usuario
        user.tipo_usuario="Empresa"
        user.save()
        #comprobamos que se crea un perfil empresa del usuario
        self.assertTrue(EmpresaPerfil.objects.get(user=user)) 
        #comprobamos que se elimino el usuario de perfil aspirante, confirmando que no existen perfiles aspirante
        self.assertLess(AspirantePerfil.objects.all().count(),1)
    
    def test_actualizacion_empresa_a_aspirante(self):
        #se registrara un usuario ingresandole el tipo empresa
        user = User.objects.create_user(email='user@test.com', username='testuser', password='abc123',tipo_usuario="Empresa")
        user.save()
        #comprobamos que exista un perfil empresa con el usuario que se acaba de crear
        self.assertTrue(EmpresaPerfil.objects.get(user=user))
        #se actualiza el tipo usuario
        user.tipo_usuario="Aspirante"
        user.save()
        #comprobamos que se crea un perfil aspirante del usuario
        self.assertTrue(AspirantePerfil.objects.get(user=user)) 
        #comprobamos que se elimino el usuario de perfil empresa, confirmando que no existen perfiles empresa
        self.assertLess(EmpresaPerfil.objects.all().count(),1)

class AplicarConvocatoria(TestCase):

    def setUp(self):
        user = User.objects.create_user(email='empresa@test.com', username='empresa', password='abc123',tipo_usuario="Empresa")
        empresa=EmpresaPerfil.objects.all()[0]
        self.convocatoria = Convocatoria.objects.create(cargo='Tester',descripcion='test convocatoria description',
        fecha_cierre="2020-05-01",hora_cierre="18:00:00",empresa=empresa)
        self.aspirante_anonimo=AnonimoPerfil.objects.create(nombre_completo="anonimo_test",curriculo="",id_convocatoria="1")

    def test_anonimo(self):
        anonimos_convocatoria=self.convocatoria.aspirantes_anonimos.all()
        self.assertIn(self.aspirante_anonimo,anonimos_convocatoria)
