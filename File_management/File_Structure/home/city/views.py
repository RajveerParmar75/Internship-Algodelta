from rest_framework.views import APIView
from .serializer import CityDataSerializer
from ..models import CityModel
from rest_framework.response import Response
from ..models import State
from ..views import check_position


class CityViews(APIView):
    def get(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) in "admin":
            data=CityModel.objects.all().values()
            serializer = CityDataSerializer(data=data, many=True)
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
        if check_position(auth_header) in "admin":
            data = request.data
            try:
                State.objects.get(id=data['state_id'])
                serializer = CityDataSerializer(data=data)
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
            except State.DoesNotExist:
                return Response({
                    "status": 400,
                    "data": "state not exist"
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
        if check_position(auth_header) in "admin":
            id=request.data['id']
            try:
                data=CityModel.objects.get(id=id)
                data.delete()
                return Response({
                    'status': 200,
                    'message': 'data deleted'
                })
            except CityModel.DoesNotExist:
                return Response({
                    'status': 400,
                    'message': 'not found'
                })
        else:
            return Response("you are not valid")