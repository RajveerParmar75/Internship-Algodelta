# api/views.py

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import DeviceSerializer
from django.http import HttpRequest
from models import *

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request: HttpRequest):
        devices = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(devices, many=True)
        return Response(serializer.data)

    def create(self, request: HttpRequest):
        device_name = request.data.get("device_name")

        if not device_name:
            return Response({"error": "Device Name is required."}, status=400)

        device = Device(user=request.user, device_name=device_name)
        device.save()
        serializer = self.serializer_class(device)
        return Response(serializer.data, status=201)
