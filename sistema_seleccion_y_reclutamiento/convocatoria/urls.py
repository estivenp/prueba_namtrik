from django.urls import path
from .views import (CrearConvocatoriaView,ConvocatoriasView,MisConvocatoriasView,MisConvocatoriasAspiranteView,
    DetalleConvocatoriaView)

urlpatterns = [
    path('crear_convocatoria', CrearConvocatoriaView.as_view(),name='convocatoria.crear_convocatoria'),
    path('', ConvocatoriasView.as_view(),name='convocatoria.convocatorias'),
    path('mis_convocatorias', MisConvocatoriasView.as_view(),name='convocatoria.mis_convocatorias'),
    path('convocatorias_aspirante', MisConvocatoriasAspiranteView.as_view(),name='convocatoria.convocatorias_aspirante'),
    path('detalle_convocatoria/<int:id_conv>', DetalleConvocatoriaView.as_view(),name='convocatoria.detalle_convocatoria'),
]
