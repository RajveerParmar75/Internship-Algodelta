from rest_framework.response import Response

from ...models import MonitorMobel
from .serializer import MonitorDataSerializer
from rest_framework.views import APIView

from ...views import check_position


class MonitorView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) == "admin":
            data = MonitorMobel.objects.all().values()
            serializer = MonitorDataSerializer(data=data, many=True)
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
        else:
            return Response("you are not valid")
    def post(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) == "admin":
            data=request.data
            serializer = MonitorDataSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
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