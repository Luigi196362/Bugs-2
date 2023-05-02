from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from Insectos.schema import schema
from Insectos.models import Insecto

INSECTOS_QUERY = '''
 {
   Insectos {
     id
     nombre 
     nomcientifico
     clase 
     orden 
     familia
     habitat
     dieta 
     longitud
     color
     numalas
   } 
 }
'''


class InsectoTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.Insecto1 = mixer.blend(Insecto)
        self.Insecto2 = mixer.blend(Insecto)

    def test_Insectos_query(self):
        response = self.query(
            INSECTOS_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print ("query Insectos results ")
        print (content)
        assert len(content['data']['Insectos']) == 2
