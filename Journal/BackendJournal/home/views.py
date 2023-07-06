from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserDataSerializer, TransactionDataSerializer
from .models import User, Transaction


class UserDataView(APIView):
    def get(self, request):
        data = User.objects.all().values()
        serializer = UserDataSerializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=False)
        return Response({
            'status': 200,
            "data": serializer.data
        })
    def delete(self,request):
        user = get_object_or_404(User, id=request.data['id'])
        user.delete()
        return Response({
            'status': 200,
            "data": "user is deleted"
        })
    def post(self, request):
        data = request.data
        serializer = UserDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                "data": serializer.data
            })
        else:
            return Response({
                'status': False,
                "data": serializer.errors
            })

    def patch(self, request):
        reqdata = request.data
        try:
            data = User.objects.get(id=reqdata['id'])
        except User.DoesNotExist:
            return Response({
                'status': False,
                'message': 'User does not exist'
            }, status=404)

        if 'flag' in reqdata:
            if reqdata['flag'] == 'credit':
                data.money += int(reqdata.get('money', 0))
                log_data = {"user_id": data.id, "money": reqdata.get('money')}
            elif reqdata['flag'] == 'debit':
                data.money -= int(reqdata.get('money', 0))
                log_data = {"user_id": data.id, "money": reqdata.get('money'), "is_credited": False}
            else:
                return Response({
                    'status': False,
                    'message': 'Enter a valid flag (credit or debit)'
                }, status=400)

            updated_data = {'money': data.money}
            serializer = UserDataSerializer(data, data=updated_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(log_data)
            serializerT = TransactionDataSerializer(data=log_data)
            if serializerT.is_valid():
                serializerT.save()
                return Response({
                    'status': 200,
                    'data': serializerT.data
                })
            else:
                return Response({
                    'status': 200,
                    'data': serializerT.errors
                })
        else:
            return Response({
                'status': False,
                'message': 'Enter a flag'
            }, status=400)


class TransactionDataView(APIView):
    def get(self, request,id):
        try:
            data = Transaction.objects.filter(user_id=id).values()
        except Transaction.DoesNotExist:
            return Response({
                'status': False,
                "message": "user not exist"
            })
        return Response({
            'status': 200,
            "data": list(data)
        })
