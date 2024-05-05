from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Device

from .serializers import DeviceSerializer

import json

@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':
        devices = Device.objects.all()

        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_device_by_id(request, id):

    try:
        device = Device.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)