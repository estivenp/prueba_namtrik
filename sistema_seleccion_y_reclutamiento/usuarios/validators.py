import os
from django.core.exceptions import ValidationError

# Funcion que valida que solo se suban archivos .pdf
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Solo soporta archivos .pdf')

#funcion que valida el tamaño del archivo
def validate_file_size(value):
    filesize= value.size
    
    if filesize > 10485760:
        raise ValidationError(u"El tamaño del archivo no puede superar los 10MB")
    else:
        return value
