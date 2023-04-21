import graphene
from graphene_django import DjangoObjectType

from .models import Insecto


class InsectoType(DjangoObjectType):
    class Meta:
        model = Insecto


class Query(graphene.ObjectType):
    insectos = graphene.List(InsectoType)

    def resolve_insectos(self, info, **kwargs):
        return Insecto.objects.all()
    
    

    # ...code
#1
class CreateInsecto(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    nomcientifico = graphene.String()
    clase= graphene.String()
    orden=graphene.String()
    familia=graphene.String()
    habitat=graphene.String()
    dieta=graphene.String()
    longitud=graphene.String()
    color=graphene.String()
    numalas=graphene.String()

    #2
    class Arguments:
        nombre = graphene.String()
        nomcientifico = graphene.String()
        clase= graphene.String()
        orden=graphene.String()
        familia=graphene.String()
        habitat=graphene.String()
        dieta=graphene.String()
        longitud=graphene.String()
        color=graphene.String()
        numalas=graphene.String()
    #3
    def mutate(self, info , nombre, nomcientifico, clase, orden, familia, habitat, dieta, longitud, color, numalas):
        insecto = Insecto(nombre=nombre, nomcientifico=nomcientifico, clase=clase, orden=orden, familia=familia, habitat=habitat, dieta=dieta, longitud=longitud, color=color, numalas=numalas)
        insecto.save()

        return CreateInsecto(
            id=insecto.id,
            nombre=insecto.nombre,
            nomcientifico=insecto.nomcientifico,
            clase=insecto.clase,
            orden=insecto.orden,
            familia=insecto.familia,
            habitat=insecto.habitat,
            dieta=insecto.dieta,
            longitud=insecto.longitud,
            color=insecto.color,
            numalas=insecto.numalas

        )


#4
class Mutation(graphene.ObjectType):
    create_insecto = CreateInsecto.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)