from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from ..models import CustomUser
from rest_framework import serializers
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("user created")
        token = super().get_token(user)
        token['type'] = user.type_user
        token['organization_name'] = user.organization_name
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
                token = serializer.validated_data.get('access')
                return Response({
                    'status': True,
                    'message': 'Token generated successfully',
                    'data': {
                        'token': str(token)
                    }
                })
            except serializers.ValidationError as e:
                return Response({
                    'status': False,
                    'message': 'Validation Error',
                    'data': e.detail
                })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error',
                'data': str(e)
            })
