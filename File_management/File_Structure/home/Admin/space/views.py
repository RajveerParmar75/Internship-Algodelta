from rest_framework.response import Response
from rest_framework.views import APIView
from ...models import SpaceModel,OrganizationModel
from .serializer import SpaceDataSerializer
from ...views import check_position


class SpaceView (APIView):
    def get(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) == "admin":
            data=SpaceModel.objects.all()
            serializer = SpaceDataSerializer(data=data, many=True)
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
        data = request.data
        try:
           OrganizationModel.objects.get(id=data['organization_id'])
        except SpaceModel.DoesNotExist:
            return Response({"org not exist"})
        serializer =SpaceDataSerializer(data=data)
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
