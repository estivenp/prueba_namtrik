"""ssr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls',), name='usuarios' ),
    path('', include('convocatoria.urls',), name='convocatoria' ),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'),
        name='login'),
    path('logout', auth_views.logout_then_login, name='logout'),

    path('password_reset', auth_views.PasswordResetView.as_view(template_name='reset_pass/password_reset_form.html',
    email_template_name='reset_pass/password_reset_email.html'),name='password_reset'),

    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='reset_pass/password_reset_done.html')
    ,name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_pass/password_reset_confirm.html')
    ,name='password_reset_confirm'),

    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='reset_pass/password_reset_complete.html')
    ,name='password_reset_complete'),

    path('apis/', include('apis.urls'), name='apis')
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)