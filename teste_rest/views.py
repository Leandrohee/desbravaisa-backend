# ----------------------------- BUSINESS LOGIC + RENDER IN THE SCREN ----------------------------- #

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pessoas
from .serializer import PessoasSerializer
from django.http import HttpResponse

# ------------------------------------------ HOME ROUTE ------------------------------------------ #
def index(request):
    return HttpResponse(
        """
        <h1>Teste_rest route</h1>    
        """
    )

# ------------------------------------------ REST ROUTES ----------------------------------------- #
@api_view(['GET'])
def get_pessoas(req):
    pessoas = Pessoas.objects.all()
    serializer = PessoasSerializer(pessoas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_pessoa(req):
    #Serializing the data send form the front-end
    serializer  = PessoasSerializer(data=req.data)

    #Checking if is valid, then saving in the DB
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_pessoa(req, pk):
    try:
        pessoa = Pessoas.objects.get(pk=pk)
    except Pessoas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = PessoasSerializer(pessoa)
        return Response(serializer.data)
    
    elif req.method == 'PUT':
        serializer = PessoasSerializer(pessoa, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif req.method == 'DELETE':
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ------------------------------------------- EXAMPLES ------------------------------------------- #
''''
GET -> localhost:3000/teste_rest/get

POST -> localhost:3000/teste_rest/create
    {
        "age": 27,
        "name": "Rafael Torres",
        "sex": "Male",
        "birth": "1997-09-07T00:00:00"
    }

PUT ->  localhost:3000/teste_rest/get/3
Changing the age to 50
    {
        "cod_pessoa": 3,
        "age": 30,
        "name": "Leandro Torres",
        "sex": "Male",
        "married": false,
        "birth": "1994-11-14T17:23:55-02:00",
        "info": ""
    }

Changing the info
    {
        "cod_pessoa": 3,
        "age": 50,
        "name": "Leandro Henrique Torres",
        "sex": "Male",
        "married": false,
        "birth": "1994-11-14T17:23:55-02:00",
        "info": "now i have a info"
    }

DELET -> localhost:3000/teste_rest/get/6
    Click the delete buttonn

'''


