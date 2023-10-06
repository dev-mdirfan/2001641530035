from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 
# from base.models import Item
# from .serializers import ItemSerializer

class HelloView(APIView): 
    permission_classes = (IsAuthenticated, ) 
    def get(self, request): 
        content = {'message': 'Hello'} 
        return Response(content) 

