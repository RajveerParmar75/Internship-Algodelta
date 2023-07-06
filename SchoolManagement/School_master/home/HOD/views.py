from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import HodSerializer
from .models import Hod
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class HodView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    def get_queryset(self):
        return Hod.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = HodSerializer(queryset, many=True)
        return Response({
            'status': 200,
            'message': 'Teacher data',
            'data': serializer.data
        })
