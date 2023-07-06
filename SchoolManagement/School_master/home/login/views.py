from rest_framework.decorators import APIView
from rest_framework.response import Response
from ..Token.models import CustomUser
from ..Token.views import MyTokenObtainPairSerializer
from ..Register.models import Register
from .serializer import LoginDataSerializer
class LoginUserView(APIView):
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data)
            username = data.get('email')
            if username is None:
                return Response({
                    'status': False,
                    'message': 'Email is missing',
                    'data': []
                })

            try:
                user = CustomUser.objects.get(email=username)
                print(user.id, "user")
                print(data, "data")
            except CustomUser.DoesNotExist:
                return Response({
                    'status': False,
                    'message': 'User does not exist',
                    'data': []
                })
            #
            # serializer = self.
            # serializer.is_valid(raise_exception=True)
            # token = serializer.validated_data.get('access')

            return Response({
                'status': True,
                'message': 'Token generated successfully',
                'data': {
                    'token': str()
                }
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error',
                'data': []
            })