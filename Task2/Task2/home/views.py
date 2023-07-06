from rest_framework.decorators import api_view, APIView, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserDataSerializer

@api_view()
@permission_classes([IsAuthenticatedOrReadOnly])
def get(request):
        trade_obj = User.objects.all()
        serializer = UserDataSerializer(trade_obj, many=True)
        return Response({
            'status': True,
            'message': 'fetch data  ',
            'data': serializer.data
        })
@api_view(['POST'])
@permission_classes([AllowAny])
def post(request):
    try:
        data = request.data
        serializer = UserDataSerializer(data=data)
        if serializer.is_valid():
            # data={"username":data['username'],"password":data['password'],"mac":mac_address}
            serializer.save()
            return Response({
                'status': True,
                'message': 'Done  ',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'bad data ',
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Error ',
    })