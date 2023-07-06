from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from ..Token.models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("user ======")
        token = super().get_token(user)
        token['email'] = user.email
        token['position'] = user.position
        return token


class MyTokenObtainPairView(TokenObtainPairView):
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

            serializer = self.get_serializer(data=data)
            try:
                serializer.is_valid(raise_exception=True)
                print("done")
                token = serializer.validated_data.get('access')
                return Response({
                    'status': True,
                    'message': 'Token generated successfully',
                    'data': {
                        'token': str(token)
                    }
                })
            except Exception as e:
                return Response({
                    'status': False,
                    'message': 'bad request',
                    'data':serializer.errors
                })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error',
                'data': []
            })
