from django.contrib import admin
from .models import Usuario, EmpresaPerfil, AspirantePerfil, AnonimoPerfil
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# admin.site.register(Usuario)
# @admin.register(EmpresaPerfil)
# @admin.register(AspirantePerfil)


class UserAdmin(BaseUserAdmin):

    # los campos que seran utlizados para mostrar el modelo de usuario
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Informacion personal', {'fields': ('first_name', 'last_name')}),
        ('Tipo', {'fields': ('tipo_usuario',)}),
        ('Grupos', {'fields': ('groups',)}),
        ('Permisos django', {
         'fields': ('is_superuser', 'is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': ('email', 'username', 'password1', 'password2')
         }
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(AnonimoPerfil)
admin.site.register(EmpresaPerfil)
admin.site.register(AspirantePerfil)
admin.site.register(Usuario, UserAdmin)
