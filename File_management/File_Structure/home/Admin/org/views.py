from rest_framework.response import Response
from rest_framework.views import APIView
from ...models import OrganizationModel
from .serializer import OrganizationDataSerializer
from ...views import check_position


class OrganizationView (APIView):
    def get(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) in "admin":
            data=OrganizationModel.objects.all()
            serializer = OrganizationDataSerializer(data=data, many=True)
            if serializer.is_valid():
                return Response({
                    "status": 200,
                    "data": serializer.data
                })
            else:
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
            serializer = OrganizationDataSerializer(data=data)

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