from django.shortcuts import render

# Create your views here.

#test API

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_api(request):
    data = {
        'message': 'Hello World! - This is a test API endpoint.',
        'image_url': 'https://media.istockphoto.com/id/157030584/vector/thumb-up-emoticon.jpg?s=612x612&w=0&k=20&c=GGl4NM_6_BzvJxLSl7uCDF4Vlo_zHGZVmmqOBIewgKg='
    }
    return Response(data)