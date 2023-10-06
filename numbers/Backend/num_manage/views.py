from django.shortcuts import render

# Create your views here.

import requests
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MergedNumbers
from .serializers import MergedNumbersSerializer

@api_view(['GET'])
def get_numbers(request):
    urls = request.GET.getlist('url', [])
    merged_numbers = set()

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                merged_numbers.update(data.get('numbers', []))
        except requests.exceptions.Timeout:
            # Ignore URLs that take too long to respond
            pass
        except requests.exceptions.RequestException:
            # Handle other request errors if needed
            pass

    merged_numbers = sorted(list(merged_numbers))
    serializer = MergedNumbersSerializer(data={'numbers': merged_numbers})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
