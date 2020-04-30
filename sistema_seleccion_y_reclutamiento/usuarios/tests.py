from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import AspirantePerfil,EmpresaPerfil

User=get_user_model()
# Create your tests here.

class RegistroUsuarioTestCase(TestCase):
    
    def test_registro_aspirante(self):
        #al crear un usuario por defecto se crea como tipo aspirante, se crea un perfil de usuario
        # con una instancia del usuario creado
        user = User.objects.create_user(email='user@test.com', username='testuser', password='abc123')
        user.save()
        aspirante=AspirantePerfil.objects.all()[0]#obtenenos al usuario perfil aspirante que se acaba de crear
        self.assertEqual(user, aspirante.user)#comprobamos que el perfil que se creo es de aspirante 
    
    def test_registro_empresa(self):
        #se registrara un usuario ingresandole el tipo empresa
        user = User.objects.create_user(email='user@test.com', username='testuser', password='abc123',tipo_usuario="Empresa")
        user.save()
        empresa=EmpresaPerfil.objects.all()[0]#obtenenos al usuario perfil empresa que se acaba de crear
        self.assertEqual(user, empresa.user)#comprobamos que el perfil que se creo es de empresa 
