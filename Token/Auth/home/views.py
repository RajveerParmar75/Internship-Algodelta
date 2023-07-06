from pprint import pprint

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User,City, State
from .serializers import UserDataSerializer,CitySerializer, StateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] =user.username
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
@api_view()
def get(request):
        trade_obj = User.objects.all()
        serializer = UserDataSerializer(trade_obj, many=True)
        return Response({
            'status': True,
            'message': 'fetch data  ',
            'data': serializer.data
        })
@api_view(['POST'])
def post(request):
    try:
        client_ip = request.META.get('REMOTE_ADDR')
        data = request.data|{"device_ip":client_ip}
        serializer = UserDataSerializer(data=data)
        pprint(client_ip)
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
@api_view()
def get_city(request):
    city=City.objects.all()
    print(city)
    print(city.values())
    print(list(city.values('name','state__name')))
    return Response({
        'status': True,
        'message': 'fetch data  ',
        'data': []
    })
@api_view(['POST'])
def create_city(request):
    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        # Get the state object or create a new state if it doesn't exist
        state_name = request.data.get('state')
        state, _ = State.objects.get_or_create(name=state_name)

        # Set the state object in the city serializer
        serializer.validated_data['state'] = state

        # Save the city object
        city = serializer.save()

        return Response({
            'status': True,
            'message': 'City created successfully',
            'data': serializer.data
        })
    return Response({
        'status': False,
        'message': 'Invalid data',
        'errors': serializer.errors
    })