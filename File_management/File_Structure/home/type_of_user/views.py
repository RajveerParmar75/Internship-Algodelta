from rest_framework.views import APIView
from .serializer import User_TypeModelSerializer
from ..models import User_TypeModel
from rest_framework.response import Response

from ..views import check_position


class User_TypeViews(APIView):
    def get(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) == "admin":
            data=User_TypeModel.objects.all()
            serializer =User_TypeModelSerializer(data=data, many=True)
            serializer.is_valid(raise_exception=False)
            return Response({
                "status": 200,
                "data": serializer.data
            })
        else:
            return Response("you are not valid")
    def post(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) == "admin":
            data = request.data
            serializer = User_TypeModelSerializer(data=data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response({
                    "status": 200,
                    "data": serializer.data
                })
            else:
                return Response({
                    "status": 400,
                    "data": serializer.errors
                })
        else:
            return Response("you are not valid")
    def delete(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) == "admin":
            id=request.data['id']
            try:
                data=User_TypeModel.objects.get(id=id)
                data.delete()
                return Response({
                    'status': 200,
                    'message': 'data deleted'
                })
            except User_TypeModel.DoesNotExist:
                return Response({
                    'status': 400,
                    'message': 'not found'
                })
        else:
            return Response("you are not valid")
