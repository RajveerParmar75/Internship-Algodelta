import jwt
from django.shortcuts import render
from rest_framework.decorators import APIView


# Create your views here.
def check_position(token):
    decoded_token = jwt.decode(token, 'django-insecure-7c4^21w6r&=hw7gz7o7(@n4pd&yg*-$7f!+h0k87_g=%7#wle0',
                               algorithms=['HS256'])
    if decoded_token['position'] == 'student':
        return 'student'
    elif decoded_token['position'] == 'teacher':
        return 'teacher'
    elif decoded_token['position'] == 'hod':
        return 'hod'

