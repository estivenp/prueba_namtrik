from django.urls import path
from .views import SignupView,UsuarioAnonimoView,UsuarioAspiranteUpdate

urlpatterns = [
    path('signup', SignupView.as_view(), name='usuarios.signup'),
    path('usuario_anonimo/<int:pk>', UsuarioAnonimoView.as_view(), name='usuarios.usuario_anonimo'),
    path('usuario_aspirante/<int:pk>/<int:id_conv>', UsuarioAspiranteUpdate.as_view(), name='usuarios.usuario_aspirante'),
]
