from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import GradeSerializer
from .models import Grade
from ..Teacher.models import Teacher
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from ..views import check_position
class GradeView(APIView):
    def get_queryset(self):
        return Grade.objects.all()
    def formated_data(self,data):
        new_list=[]
        for i in data:
            teacher_data = Teacher.objects.get(id=i['teacher_id'])
            new_list.append({"name":teacher_data.name,"expense":teacher_data.money*i['rank']})
            print(data)
        return new_list
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })

        # Check the user's position

        if check_position(auth_header) == "hod":
            queryset = self.get_queryset()
            serializer = GradeSerializer(queryset, many=True)
            data=serializer.data
            return Response({
                'status': 200,
                'message': 'Teacher data',
                'data': self.formated_data(data)
            })
        else:
            return Response({
                'status': 400,
                'message': 'you are not hod'
            })
    def post(self,request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })

        # Check the user's position

        if check_position(auth_header) == "hod":
            serializer = GradeSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    teacher_data = Teacher.objects.get(id=serializer.validated_data['teacher_id'])
                    serializer.save()
                    return Response({
                        'status': 200,
                        'message': 'Teacher is added',
                        'data': serializer.data
                    })
                except Exception as e:
                    return Response({
                        'status': 400,
                        'message': 'enter valid teacher id',
                        'data': str(e)
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