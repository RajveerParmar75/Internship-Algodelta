import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser, AdminUser, AgentUser, Saving_account, Saving_Transection, Loan_Transection, Loan_account
from .serializer import UserDataSerializer, RegisterDataSerializer, AdminUserDataSerializer, AgentUserDataSerializer, \
    Saving_accountDataSerializer, Saving_TransectionDataSerializer, Loan_TransectionDataSerializer, Loan_DataSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("user ======")
        token = super().get_token(user)
        token['email'] = user.email
        token['type'] = user.type
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
                    'data': serializer.errors
                })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error',
                'data': []
            })


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
            if request.data.get('type') not in ["admin", 'agent']:
                return Response({
                    'status': False,
                    'message': 'enter valid type'
                }, status=status.HTTP_400_BAD_REQUEST)
            user = CustomUser.objects.create_user(
                email=serializer.data['username'],
                password=serializer.data['password'],
                type=request.data.get('type')
            )
            if request.data.get('type') == "admin":
                data = {"name": request.data['username'], "user": user.id}
                serializer_admin = AdminUserDataSerializer(data=data)
                if serializer_admin.is_valid():
                    serializer_admin.save()
                else:
                    return Response({
                        'status': False,
                        'message': 'some error occurred',
                        'data': serializer_admin.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            elif request.data.get('type') == "agent":
                if request.data.get('admin') is None:
                    return Response({
                        'status': False,
                        'message': 'enter admin id',
                    }, status=status.HTTP_400_BAD_REQUEST)
                data = {"name": request.data['username'], "user": user.id, "admin": request.data.get('admin')}
                serializer_agent = AgentUserDataSerializer(data=data)
                if serializer_agent.is_valid():
                    serializer_agent.save()
                else:
                    return Response({
                        'status': False,
                        'message': 'some error occurred',
                        'data': serializer_agent.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            if serializer.is_valid():
                return Response({
                    'status': True,
                    'message': 'User is registered',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': False,
                    'message': 'some error occurred',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error in token',
                'data': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class AdminRegister(APIView):
    def isAdmin(self, id):
        try:
            user = CustomUser.objects.get(id=id)
            return True if str(user.type).lower() == "admin" else False
        except CustomUser.DoesNotExist:
            return None

    def get(self, request):
        user = AdminUser.objects.all()
        serializer = AdminUserDataSerializer(user, many=True)

        # user = CustomUser.objects.create_user(email="data@gmail.com", password='123')
        # print(user)
        return Response({
            'status': True,
            'message': 'fetch data',
            'data': serializer.data
        })

    def post(self, request):
        serializer = AdminUserDataSerializer(data=request.data)
        temp = self.isAdmin(request.data['user_id'])
        if serializer.is_valid() and temp:
            serializer.save()
            return Response({
                "status": True,
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        elif not temp:
            return Response({
                "status": False,
                "message": "you are not ADMIN"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "status": False,
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class AgentRegister(APIView):
    def isAgent(self, id):
        try:
            user = CustomUser.objects.get(id=id)
            return True if str(user.type).lower() == "agent" else False
        except CustomUser.DoesNotExist:
            return None

    def get(self, request):
        user = AgentUser.objects.all()
        serializer = AgentUserDataSerializer(user, many=True)

        # user = CustomUser.objects.create_user(email="data@gmail.com", password='123')
        # print(user)
        return Response({
            'status': True,
            'message': 'fetch data',
            'data': serializer.data
        })

    def post(self, request):
        serializer = AgentUserDataSerializer(data=request.data)
        temp = self.isAgent(request.data['user_id'])
        if serializer.is_valid() and temp:
            serializer.save()
            return Response({
                "status": True,
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        elif not temp:
            return Response({
                "status": False,
                "message": "you are not AGENT"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "status": False,
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class Saving_accountView(APIView):
    def FileUplode(self, data):
        path = f"../document/{data['agent_id']}/{data['user_id']}/{data['file'].name}"
        # if not os.path.exists(path):
        base_directory = '../document'
        org_directory = os.path.join(base_directory, f"{data['agent_id']}")
        data_directory = os.path.join(org_directory, f"{data['user_id']}")
        os.makedirs(data_directory, exist_ok=True)
        uploaded_file = data['file']
        file_content = uploaded_file.read()
        with open(path, 'wb') as file:
            file.write(file_content)
        return Response({
            'status': 200,
            'message': 'Data uploaded successfully.'
        })

    def get(self, request):
        user = Saving_account.objects.all().values()
        return Response({
            "status": True,
            "data": user
        })

    def delete(self, request):
        id = request.GET.get("id")
        if id is None:
            return Response({
                "status": False,
                "message": "enter id"
            })
        try:
            data = Saving_account.objects.get(id=id)
            data.delete()
            return Response({
                "status": True,
                "message": "Account deleted successfully."
            })
        except Saving_account.DoseNotExist:
            return Response({
                "status": False,
                "message": "user does not exist."
            })

    def post(self, request):
        serializer = Saving_accountDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.FileUplode(
                {"agent_id": serializer.data['id'], 'file': request.data['file'], 'user_id': serializer.data['id']})
            return Response({
                "status": True,
                'data': serializer.data
            })
        else:
            return Response({
                "status": False,
                'data': serializer.errors
            })


class Saving_TransectionView(APIView):
    def get(self, request):
        data = Saving_Transection.objects.all().values()

        return Response({
            "status": False,
            "data": list(data)
        }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data
        serializer = Saving_TransectionDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": False,
                "message": "invalid",
                "error": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class Loan_accountView(APIView):
    def get(self, request):
        user = Loan_account.objects.all().values()
        return Response({
            "status": True,
            "data": list(user)
        }, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.GET.get("id")
        if id is None:
            return Response({
                "status": False,
                "message": "enter id"
            })
        try:
            data = Loan_account.objects.get(id=id)
            data.delete()
            return Response({
                "status": True,
                "message": "Account deleted successfully."
            })
        except Loan_account.DoseNotExist:
            return Response({
                "status": False,
                "message": "user does not exist."
            })

    def post(self, request):
        serializer = Loan_DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                'data': serializer.data
            })
        else:
            return Response({
                "status": False,
                'data': serializer.errors
            })


class Loan_TransectionView(APIView):
    def get(self, request):
        data = Loan_Transection.objects.all().values()
        return Response({
            "status": True,
            "data": list(data)
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = Loan_TransectionDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": False,
                "message": "invalid"
            }, status=status.HTTP_400_BAD_REQUEST)
