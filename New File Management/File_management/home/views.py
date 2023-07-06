from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserDataSerializer, RegisterDataSerializer, UploadDataSerializer
from .models import CustomUser
from .models import Organization, Document
from .serializer import OrganizationDataSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import os
import jwt


# Create your views here.
def check_position(token):
    decoded_token = jwt.decode(token, 'django-insecure-7%=dw8q45bh8^yej0ewhh-v^g5e!tan+cac2s^max7v%xf380l',
                               algorithms=['HS256'])
    if decoded_token['type_user'] == 1:
        return 'user', decoded_token['org_id'], decoded_token['user_id']
    elif decoded_token['type_user'] == 2:
        return 'org', decoded_token['org_id'], decoded_token['user_id']
    elif decoded_token['type_user'] == 3:
        return 'admin', 0, 0


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

            organization_id = request.data['organization_name']
            organization = Organization.objects.get(id=organization_id)

            user = CustomUser.objects.create_user(
                email=serializer.data['username'],
                password=serializer.data['password'],
                type_user=request.data['type'],
                mobile_number=request.data['mobile_number'],
                city=request.data['city'],
                state=request.data['state'],
                organization_name=organization
            )

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
    def patch(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if ['user', 'org'] in check_position(auth_header):
            User = get_user_model()
            data = request.data
            user = User.objects.get(email=data['username'])
            new_password = make_password(data['password'])
            user.password = new_password
            user.save()
            return Response({
                "msg": "pass is changed",
                "data": user.email
            })
        else:
            return Response("you are not valid")


class UploadFile(APIView):
    def delete(self, request):
        user = Document.objects.get(id=request.data['id'])
        serializer = UploadDataSerializer(data=user, many=True)
        # user = CustomUser.objects.create_user(email="data@gmail.com", password='123')
        # print(user)
        serializer.is_valid(raise_exception=True)
        user.delete()
        return Response({
            'status': True,
            'message': 'fetch data',
            'data': serializer.data
        })

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        type, org_id, user_id = check_position(auth_header)
        if type == "user":
            user = Document.objects.filter(user_id=user_id, org_id=org_id)
            serializer = UploadDataSerializer(user, many=True)
            # user = CustomUser.objects.create_user(email="data@gmail.com", password='123')
            # print(user)
            return Response({
                'status': True,
                'message': 'fetch data',
                'data': serializer.data
            })
        elif type == "org":
            user = Document.objects.filter(org_id=org_id)
            serializer = UploadDataSerializer(user, many=True)
            # user = CustomUser.objects.create_user(email="data@gmail.com", password='123')
            # print(user)
            return Response({
                'status': True,
                'message': 'fetch data',
                'data': serializer.data
            })
        else:
            return Response({
                'status': False,
                'message': 'you are not valid',
            })

    def post(self, request):
        data = request.data
        if 'title' in data and 'org_id' in data and 'user_id' in data:
            data['title'] = data['file'].name
            serializer = UploadDataSerializer(data=data)
            try:
                user = CustomUser.objects.get(id=data['user_id'])
                if not user.organization_name == int(data['org_id']):
                    return Response({
                        'status': 404,
                        'message': 'user not exist with your org'
                    })
            except CustomUser.DoesNotExist:
                return Response({
                    'status': 404,
                    'message': 'user not exist'
                })
            if serializer.is_valid():
                path = f"../document/{data['org_id']}/{data['user_id']}/{data['file'].name}"
                # if not os.path.exists(path):
                base_directory = '../document'
                org_directory = os.path.join(base_directory, f"{data['org_id']}")
                data_directory = os.path.join(org_directory, f"{data['user_id']}")
                os.makedirs(data_directory, exist_ok=True)
                uploaded_file = data['file']
                file_content = uploaded_file.read()
                with open(path, 'wb') as file:
                    file.write(file_content)
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Data uploaded successfully.'
                })
            else:
                return Response({
                    'status': 400,
                    'errors': serializer.errors
                })
        else:
            return Response({
                'status': 400,
                'message': 'Missing required fields in the data.'
            })
        #
        # file_content = uploaded_file.read()
        # file_size = uploaded_file.size
        # directory = Path(f"../document")
        # directory.mkdir()
        # return Response({"hello"})


class OrganizationViews(APIView):
    def get(self, request):
        user = Organization.objects.all().values()
        print(user)
        data = list(user)
        serializer = OrganizationDataSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response({
                "status": 200,
                "data": serializer.data
            })
        else:
            return Response({
                "status": 400,
                "data": serializer.errors
            })

    def post(self, request):
        serializer = OrganizationDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": 200,
            "data": serializer.data
        })
class AdminView(APIView):

    def formated_data(self,raw_data):
        new_data = []
        for i in raw_data:
            docs=Document.objects.filter(org_id=i['id'])
            serializer=UploadDataSerializer(data=docs,many=True)
            if serializer.is_valid():
                print(serializer.data)
            else:
                print(serializer.data)

            # new_data.append({docs.org_name})
    def get(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        type, org_id, user_id = check_position(auth_header)
        if type=='admin':
            user = Organization.objects.all().values()
            self.formated_data(user)
            return Response({"hello"})
            # if serializer.is_valid():
            #     return Response({
            #         'status': 200,
            #         'data': serializer.data
            #     })
            # else:
            #     return Response({
            #         'status': 401,
            #         'data': serializer.data
            #     })
        else:

            return Response({
                'status': 401,
                'message': 'you are not admin'
            })

