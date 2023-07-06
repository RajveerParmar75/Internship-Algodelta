from pprint import pprint
from rest_framework.views import APIView
from .serializer import DocsDataSerializer
from ...models import Docs,OrganizationModel
from rest_framework.response import Response

from ...views import check_position


class DocsViews(APIView):
    def is_full(self,org_name,add_space):
        data = Docs.objects.filter(org_name=org_name)
        occupied =0
        for i in data:
            occupied+=i.document.size
        try:
            print(org_name)
            org=OrganizationModel.objects.get(organization_name=org_name)

            if org.space > (occupied + add_space):
                return True
            else:
                return False
        except OrganizationModel.DoesNotExist:
            print("org dose not exist")


    def get(self,request):
        data=Docs.objects.all()
        serializer = DocsDataSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response({
                "status": 200,
                "data": serializer.data
            })
        else:
            return Response({
                "status": 200,
                "data": serializer.errors
            })

    def post(self, request):
        data = request.data
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header)=='org':
            if not self.is_full(data['org_name'],int(data['document'].size)):
                return Response({
                    "status": 400,
                    "message":"space is full"
                })
            serializer = DocsDataSerializer(data=data)
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
            return Response({
                "message":"you are not valid"
            })
    def delete(self,request):
        id=request.data['id']
        try:
            data=Docs.objects.get(id=id)
            data.delete()
            return Response({
                'status': 200,
                'message': 'data deleted'
            })
        except Docs.DoesNotExist:
            return Response({
                'status': 400,
                'message': 'not found'
            })
