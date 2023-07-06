import jwt
import traceback
from pprint import pprint

from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, SlidingToken, Token, BlacklistMixin
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import APIView, api_view
from django.contrib.auth import authenticate

from .models import Register, CustomUser, Session, City
from .serializers import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print(user.mac, "user ======")
        token = super().get_token(user)
        token['name'] = user.email
        token['is_staff'] = user.is_staff
        return token

def is_valid(token):
    decoded_token = jwt.decode(token, 'django-insecure-ij5wu__4+&596yw!bey1r%)rfpc#r=mlrny-l$!6vm1na1#f^l',
                               algorithms=['HS256'])
    if decoded_token['is_staff'] == -1:
        return False
    return True
def is_admin(token):
    decoded_token = jwt.decode(token, 'django-insecure-ij5wu__4+&596yw!bey1r%)rfpc#r=mlrny-l$!6vm1na1#f^l',
                               algorithms=['HS256'])
    if decoded_token['is_staff'] == 0:
        return True
    return False
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
            serializer.is_valid(raise_exception=True)
            token = serializer.validated_data.get('access')
            # print(serializer.data,"data.......")
            print("hello:::::")
            data1 = {
                'token': token,
                "user_id": user.id,
                'mac': data['mac'],
                "ip": data['ip'],
                "status": True,
                "username": data['email'],
            }
            serializer1 = SessionDataSerializer(data=data1)
            if serializer1.is_valid():
                print("added to session log")
                serializer1.save()
                print(serializer1.data)
            else:
                print(serializer1.errors)
            return Response({
                'status': True,
                'message': 'Token generated successfully',
                'data': {
                    'token': str(token)
                }
            })

        except Exception as e:
            print(traceback.format_exc())
            return Response({
                'status': False,
                'message': 'Error',
                'data': []
            })


@api_view(['POST'])
def login(request):
    pass


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
            data = request.data
            serializer = RegisterDataSerializer(data=data)
            if serializer.is_valid():
                user = CustomUser.objects.create_user(email=serializer.data['username'],
                                                          password=serializer.data['password'],is_staff=request.data['is_staff'])
                return Response({
                    'status': True,
                    'message': 'Done  ',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'bad data ',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Error ',
        })


class LoginUserView(APIView):
    def post(self, request):
        try:
            data = request.data
            print(data)
            try:
                CustomUser.objects.get(username=data['username'])
            except Register.DoseNotExist:
                return Response({
                    'status': False,
                    'message': 'User not exists...',
                    "data": []
                })
            serializer = LoginDataSerializer(data=data)
            print(data)
            if serializer.is_valid():
                # serializer.save()
                user = {
                    "username": serializer.data['username'],
                    'password': serializer.data['password']
                }
                token = MyTokenObtainPairSerializer.get_token(user=user)
                return Response({
                    'status': True,
                    'message': 'Done',
                    'data': token
                })
            return Response({
                'status': False,
                'message': 'bad data ',
                'data': serializer.errors
            })
        except Exception as e:
            print(traceback.format_exc())
            return Response({
                'status': False,
                'message': 'Error ',
                "data": []
            })


class SessionView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if check_token(auth_header):
            if is_valid(auth_header):
                print(auth_header)
                decoded_token = jwt.decode(auth_header, 'django-insecure-ij5wu__4+&596yw!bey1r%)rfpc#r=mlrny-l$!6vm1na1#f^l',
                                           algorithms=['HS256'])
                print(decoded_token)
                if auth_header is None:
                    return Response({
                        'status': False,
                        'message': 'Send token',
                        'data': []
                    }, status=status.HTTP_400_BAD_REQUEST)
                elif 'is_staff' in decoded_token and decoded_token['is_staff'] == 0:
                    session = Session.objects.filter(user_id=decoded_token['user_id'],status=True)
                    serializer = SessionDataSerializer(session, many=True)
                    return Response({
                        'status': True,
                        'message': 'Fetch data',
                        'data': serializer.data
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        'status': False,
                        'message': 'User is not authorized',
                        'data': []
                    }, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({
                    'status': False,
                    'message': 'token is not valid',
                    'data': []
                }, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'message': 'token is no more valid.....'}, status=status.HTTP_404_NOT_FOUND)


    def patch(self, request):
        auth_header = request.headers.get('Authorization')
        pk=request.data['id']
        try:
            session = Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            return Response({'message': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SessionDataSerializer(session, data={'status':False,'is_staff':-1}, partial=True)
        if serializer.is_valid():
            blacklistToken(auth_header)
            serializer.save()
            # token = BlacklistMixin.blacklist()
            # token.set_exp()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def blacklistToken(token):
    serializers=BlackListTokenSerializer(data={'token':token})
    if serializers.is_valid():
        print("done")
        serializers.save()
        return 'token is blacklisted'
    else:
        print( serializers.errors)
def check_token(token):
    if BlackListToken.objects.filter(token=token).exists():
        return False
    return True
class StateListAPIView(APIView):
    def post(self, request):
        data = request.data
        auth_header = request.headers.get('Authorization')
        if check_token(auth_header) and is_admin(auth_header):
            print(data)
            serializer = StateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'State created successfully',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': False,
                    'message': 'Error',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': False,
                'message': 'You are not admin or token is not valid ',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

class CityListAPIView(APIView):
    def post(self, request):
        data = request.data
        auth_header = request.headers.get('Authorization')
        if check_token(auth_header):
            if is_valid(auth_header) and is_admin(auth_header):
                serializer = CitySerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status': True,
                        'message': 'State created successfully',
                        'data': serializer.data
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        'status': False,
                        'message': 'Error',
                        'data': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'status': True,
                    'message': 'you are not admin',
                    'data': []
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': False,
                'message': 'You are not admin or token is not valid ',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

