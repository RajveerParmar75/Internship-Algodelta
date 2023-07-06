from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserDataSerializer, RegisterDataSerializer
from ..models import CustomUser
from ..models import State
from ..models import CityModel
class RegisterView(APIView):
    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserDataSerializer(user, many=True)
        # user = CustomUser.objects.create_user(email="data@gmail.com", password='123')
        # print(user)
        return Response({
            'status': True,
            'message': 'fetch data',
            'data': serializer.data
        })

    def post(self, request):
        try:
            serializer = RegisterDataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = CustomUser.objects.create_user(
                email=serializer.data['username'],
                password=serializer.data['password'],
                type_user=request.data['type'],
                mobile_number=request.data['mobile_number'],
                city=request.data['city'],
                state=request.data['state'],
                organization_name=request.data['organization_name']
            )
            State.objects.get(id=request.data['state'])
            CityModel.objects.get(id=request.data['city'])
            return Response({
                'status': True,
                'message': 'User is registered',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error',
                'data': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)