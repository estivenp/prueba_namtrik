from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uj4mk+x$4lufp15v96pdrj81*#*jt4yonj#89z23n4d+x+*pdn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sistema.seleccion.reclutamiento@gmail.com'
EMAIL_HOST_PASSWORD = 'seleccion_y_reclutamiento'
EMAIL_PORT = 25
EMAIL_USE_TLS = True