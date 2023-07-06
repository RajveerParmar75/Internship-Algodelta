from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from ..views import check_position

class StudentView(APIView):
    def get_queryset(self):
        return Student.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        return Response({
            'status': 200,
            'message': 'Teacher data',
            'data': serializer.data
        })
    def post(self, request):
        # Check if the user is authenticated
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })

        # Check the user's position
        if check_position(auth_header) in ["hod","teacher"]:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Teacher is added',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'add valid data',
                    'data': serializer.errors
                })
        else:
            return Response({
                'status': 400,
                'message': 'you are not hod'
            })

    def patch(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })

        # Check the user's position
        if check_position(auth_header) in ["hod",'teacher']:
            pk = request.data['id']
            if pk is None:
                return Response({
                    'status': 400,
                    'message': 'enter id'
                })
            try:
                data = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response({
                    'status': 400,
                    'message': 'not exist'
                })

            serializer = StudentSerializer(data, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                # token = BlacklistMixin.blacklist()
                # token.set_exp()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 400,
                'message': 'you are not hod'
            })
    def delete(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })

        # Check the user's position
        if check_position(auth_header) in ["hod",'teacher']:
            pk=request.data["id"]
            if pk is None:
                return Response({
                    'status': 400,
                    'message': 'enter id'
                })
            else:
                try:
                    teacher=Student.objects.get(pk=pk)
                    teacher.delete()
                    return Response({
                        'status': 400,
                        'message': 'user deleted'
                    })
                except Student.DoesNotExist:
                    return Response({
                        'status': 400,
                        'message': 'not found'
                    })
 