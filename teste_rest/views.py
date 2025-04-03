# ----------------------------- BUSINESS LOGIC + RENDER IN THE SCREN ----------------------------- #

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pessoas
from .serializer import PessoasSerializer


@api_view(['GET'])
def get_pessoas(req):
    return Response(PessoasSerializer())

@api_view(['POST'])
def create_pessoa(req):
    #Serializing the data send form the front-end
    serializer  = PessoasSerializer(data=req.data)

    #Checking if is valid, then saving in the DB
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

