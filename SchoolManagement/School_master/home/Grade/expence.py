from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..views import check_position
from ..Teacher.models import Teacher
from .models import Grade


@api_view(['GET'])
def get_expence(request):
    auth_header = request.headers.get('Authorization')
    which =request.GET.get('data')
    if auth_header is None:
        return Response({
            'status': 401,
            'message': 'Authentication credentials were not provided.'
        })
    if check_position(auth_header) == "hod":
        if which=="all":
            pass
        teacher_id = request.GET.get('id')
        teacher_data = Teacher.objects.get(id=teacher_id)
        grade_data = Grade.objects.get(teacher_id=teacher_id)
        data = [{
            "name": teacher_data.id,
            "expence": teacher_data.money * grade_data.rank
        }]
        return Response({
            'status': 200,
            'message': 'Teacher data',
            'data': data
        })
    else:
        return Response({
            'status': 400,
            'message': 'you are not hod'
        })
