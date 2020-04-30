from django import forms
from .models import AnonimoPerfil, AspirantePerfil, Usuario
from convocatoria.models import Convocatoria
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Usuario=get_user_model()


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(RegistroUsuarioForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first name']
            user.last_name = self.cleaned_data['last name']
            if commit:
                user.save()

            return user


class UsuarioAnonimoModelForm(forms.ModelForm):
    class Meta:
        model = AnonimoPerfil
        fields = ('nombre_completo', 'curriculo')
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nombre Completo', 'minlength': 5}),
        }

    def save(self, commit=True):
        # super().save(commit=commit)
        return super().save(commit=commit)

