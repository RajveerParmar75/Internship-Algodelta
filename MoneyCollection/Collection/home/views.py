from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TransectionDataSerializer,UserDataSerializer
from .models import User,Transaction
class UserView(APIView):
    def get(self,request):
        data=User.objects.all().values()
        serializer=UserDataSerializer(data=list(data),many=True)
        if serializer.is_valid():
            return Response({
                "status":True,
                "data":serializer.data
            })
        else:
            return Response({
                "status": False,
                "data": serializer.errors
            })
    def post(self,request):
        data = request.data
        serializer = UserDataSerializer(data=data)
        if serializer.is_valid():
            return Response({
                "status": True,
                "data": serializer.data
            })
        else:
            return Response({
                "status": False,
                "data": serializer.errors
            })