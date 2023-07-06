from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

@api_view(['POST'])
def obtain_token(request):
    username = request.data.get('username')
    password = request.data.get('password')

    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            refresh_token = RefreshToken.for_user(user)
            return Response({'token': str(refresh_token.access_token)})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=400)
