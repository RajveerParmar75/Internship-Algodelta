from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from ..models import Docs
from ..Org.docs.serializer import DocsDataSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from ..views import check_position


class UserDocsView(APIView):
    def formated_data(self,raw_data):
        name=set()
        new_data=[]
        for i in raw_data:
            name.add(i['org_name'])
        for i in name:
            data=Docs.objects.filter(org_name=i)
            serializer=DocsDataSerializer(data=data,many=True)
            serializer.is_valid(raise_exception=False)
            new_data.append({str(i):serializer.data})
        return new_data

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) in ["org","user"]:
            queryset = Docs.objects.all()
            org_name=request.GET.get("org_name")
            serializer = DocsDataSerializer(data=queryset, many=True)
            serializer.is_valid(raise_exception=False)
            if org_name is None:
                return Response({
                    "status":200,
                    "data":self.formated_data(serializer.data)
                })
            else:
                queryset = Docs.objects.filter(org_name=org_name)
                serializer = DocsDataSerializer(data=queryset, many=True)
                serializer.is_valid(raise_exception=False)
                return Response({
                    "status": 200,
                    "data": self.formated_data(serializer.data)
                })
        else:
            return Response("you are not valid")
    def post(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) in "admin":
            data=request.data
            id=data['id']
            file_obj = get_object_or_404(Docs, id=id)
            response = HttpResponse(file_obj.document, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file_obj}"'
            return response
        else:
            return Response("you are not valid")

    def patch(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) in "admin":
            User = get_user_model()
            data=request.data
            user = User.objects.get(email=data['username'])
            new_password = make_password(data['password'])
            user.password = new_password
            user.save()
            return Response({
                "msg":"pass is changed",
                "data":user.email
            })
        else:
            return Response("you are not valid")