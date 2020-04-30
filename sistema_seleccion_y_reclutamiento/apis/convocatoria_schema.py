from graphene_django.forms.mutation import DjangoModelFormMutation
from convocatoria.forms import CrearConvocatoriaApiModelForm
from graphene_django import DjangoObjectType
from convocatoria.models import Convocatoria as ConvocatoriaModel
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required,permission_required

class Convocatoria(DjangoObjectType):
    class Meta:
        model = ConvocatoriaModel
        filter_fields = {
            'cargo': ['exact', 'icontains'],
            'fecha_cierre': ['gt', 'gte', 'lt', 'lte'],
            'estado': ['exact'],
            'empresa': ['exact'],
        }
        interfaces = (relay.Node,)
    
class Query(ObjectType):
    """Consultas de la app blog"""
    convocatorias = DjangoFilterConnectionField(Convocatoria)
    convocatoria = relay.Node.Field(Convocatoria)

    @login_required
    def resolve_convocatorias(self,info,*args,**kwargs):
        return ConvocatoriaModel.objects.filter(**kwargs)


class CrearConvocatoria(DjangoModelFormMutation):
    class Meta:
        form_class = CrearConvocatoriaApiModelForm

class Mutation(ObjectType):
    crear_convocatoria = CrearConvocatoria.Field()

    @login_required
    def resolve_crear_convocatoria(self,info,*args,**kwargs):
        return CrearConvocatoriaApiModelForm.objects.filter(**kwargs)

