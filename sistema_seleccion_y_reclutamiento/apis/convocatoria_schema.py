from graphene_django import DjangoObjectType
from convocatoria.models import Convocatoria as ConvocatoriaModel
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from convocatoria.forms import CrearConvocatoriaModelForm
from graphql_jwt.decorators import login_required

class Convocatoria(DjangoObjectType):
    class Meta:
        model = ConvocatoriaModel
        filter_fields = {
            'cargo': ['exact', 'icontains'],
            'fecha_cierre': ['gt', 'gte', 'lt', 'lte'],
            'estado': ['exact'],
            'empresa': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(ObjectType):
    convocatorias = DjangoFilterConnectionField(Convocatoria)
    convocatoria = relay.Node.Field(Convocatoria)

    @login_required
    def resolve_convocatoria(self, info, *args, **kwargs):
        return ConvocatoriaModel.objects.filter(**kwargs)

class ReservaMutation(DjangoModelFormMutation):
    class Meta:
        form_class = CrearConvocatoriaModelForm

class Mutation(ObjectType):
    convocatoria = ReservaMutation.Field()



