from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserDataSerializer, RegisterDataSerializer
from ..Token.models import CustomUser
from ..Student.serializer import StudentSerializer
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
                position=request.data['position']
            )
            student_data={"name":request.data["student_name"],"standard":request.data["standard"]}
            serializer1 = StudentSerializer(data=student_data)
            if serializer1.is_valid():
                serializer1.save()
            else:
                return Response({
                    'status': 400,
                    'message': 'add valid data',
                    'data': serializer.errors
                })
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