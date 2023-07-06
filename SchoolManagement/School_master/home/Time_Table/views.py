from pprint import pprint

from rest_framework import status
from rest_framework.decorators import APIView
from .models import Time_table
from .serializer import TimeTableSerializer
from rest_framework.response import Response
from ..Teacher.subject.models import Subject
from ..views import check_position
from ..Teacher.models import Teacher
from .logic import check_data_existence, formate_data,teacher_formated


class Time_Table_Views(APIView):
    def get_queryset(self):
        return Time_table.objects.all()

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        standard = request.GET.get('id')
        day = request.GET.get('day')
        teacher_id=request.GET.get('teacher_id')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })
        if check_position(auth_header) == "student":
            if standard is None:
                return Response({
                    "enter class"
                })
            elif day is not None and 0<int(day)<=6:
                try:
                    pprint(standard)
                    queryset = Time_table.objects.filter(class_name=standard,day=day)
                    serializer = TimeTableSerializer(queryset, many=True)
                    return Response({
                        'status': 200,
                        'message': 'time table',
                        'data':formate_data(serializer.data)[int(day)]
                    })
                except Time_table.DoesNotExist:
                    return Response({
                        'status': False,
                        'message': 'no data found',
                        'data': []
                    })
            elif teacher_id is not None:
                try:
                    pprint(standard)
                    queryset = Time_table.objects.filter(teacher=teacher_id,class_name=standard)
                    serializer = TimeTableSerializer(queryset, many=True)
                    return Response({
                        'status': 200,
                        'message': 'time table',
                        'data': serializer.data
                    })
                except Time_table.DoesNotExist:
                    return Response({
                        'status': False,
                        'message': 'no data found',
                        'data': []
                    })
            else:
                print("hello")
                try:
                    queryset = Time_table.objects.filter(class_name=standard)
                    serializer = TimeTableSerializer(queryset, many=True)
                    return Response({
                        'status': 200,
                        'message': 'time table',
                        'data':formate_data(serializer.data)
                    })
                except Time_table.DoesNotExist:
                    return Response({
                        'status': False,
                        'message': 'no data found',
                        'data': []
                    })
        # Check the user's position
        elif check_position(auth_header) == "hod":
            queryset = self.get_queryset()
            serializer = TimeTableSerializer(queryset, many=True)
            return Response({
                'status': 200,
                'message': 'time table',
                'data': serializer.data
            })
        elif check_position(auth_header) == "teacher":
            if standard is None:
                return Response({
                    'message':"enter id"
                })
            else:
                try:
                    pprint(standard)
                    queryset = Time_table.objects.filter(teacher=standard)
                    serializer = TimeTableSerializer(queryset, many=True)

                    return Response({
                        'status': 200,
                        'message': 'time table',
                        'data':teacher_formated(serializer.data)
                    })
                except Time_table.DoesNotExist:
                    return Response({
                        'status': False,
                        'message': 'no data found',
                        'data': []
                    })
        else:
            return Response({
                'status': 400,
                'message': 'you are not hod'
            })

    def post(self, request):
        # Check if the user is authenticated
        auth_header = request.headers.get('Authorization')
        replace = request.GET.get('repl')
        if auth_header is None:
            return Response({
                'status': 401,
                'message': 'Authentication credentials were not provided.'
            })

        # Check the user's position
        if check_position(auth_header) == "hod":
            data = request.data
            id_teacher = data['teacher']
            try:
                sub = Subject.objects.get(teacher_id=id_teacher)
                tec = Teacher.objects.get(id=id_teacher)
                print(check_data_existence(class_name=data['class_name'], day=data['day'], slot=data['slot']),
                      replace)
                if check_data_existence(class_name=data['class_name'], day=data['day'], slot=data['slot']) == False:
                    queryset = Time_table.objects.filter(teacher=id_teacher,day=data["day"])
                    serializer = TimeTableSerializer(queryset, many=True)
                    if len(serializer.data)<=tec.time:
                        new_data=data|{"subject":sub.id}
                        serializer = TimeTableSerializer(data=new_data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({
                                'status': 200,
                                'message': 'data  is added',
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
                            'message': 'limit is reached'
                        })
                elif check_data_existence(class_name=data['class_name'], day=data['day'],
                                          slot=data['slot']):
                    if 'true' == replace:
                        print("datataaatatatata")
                        queryset = Time_table.objects.filter(teacher=id_teacher, day=data["day"])
                        serializer1 = TimeTableSerializer(queryset, many=True)
                        data = Time_table.objects.get(class_name=data['class_name'], day=data['day'], slot=data['slot'])
                        serializer = TimeTableSerializer(data, request.data, partial=True)
                        if len(serializer1.data) >= tec.time:
                            return Response({"message": "limit is reached"},
                                            status=status.HTTP_403_FORBIDDEN)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"message": "lacture is updated", "data": serializer.data},
                                            status=status.HTTP_200_OK)
                        else:
                            return Response({"message": "error", "data": serializer.errors},
                                            status=status.HTTP_200_OK)
                    else:
                        return Response({"message": "proper data is not provided"},
                                        status=status.HTTP_200_OK)
                else:
                    return Response({"message": "data exist"})
            except Subject.DoesNotExist:
                return Response({
                    'status': 404,
                    'message': 'subject dosent exist',
                    'data': 'enter valid subject'
                })
            except Teacher.DoesNotExist:
                return Response({
                    'status': 404,
                    'message': 'Teacher dosent exist',
                    'data': 'enter valid teacher'
                })

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
        if check_position(auth_header) == "hod":
            pk=request.data["id"]
            if pk is None:
                return Response({
                    'status': 400,
                    'message': 'enter id'
                })
            else:
                try:
                    teacher=Time_table.objects.get(pk=pk)
                    teacher.delete()
                    return Response({
                        'status': 400,
                        'message': 'user deleted'
                    })
                except Time_table.DoesNotExist:
                    return Response({
                        'status': 400,
                        'message': 'not found'
                    })
