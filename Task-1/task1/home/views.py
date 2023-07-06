from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TradeSerialize
from rest_framework import status

from .models import Trade


def formatedData(data):
    formateddata = []
    if len(data) == 8:
        formateddata.append({
            data["name"].upper(): {
                "uuid": data["uuid"],
                "time": data["time"],
                "qnt": data["qnt"],
                "price": data["price"],
                "action": data["action"],
                "avg": data["avg"],
                "p_l": data["p_l"]
            }})
    else:
        for i in data:
            formateddata.append({
                i["name"].upper(): {
                    "uuid": i["uuid"],
                    "time": i["time"],
                    "qnt": i["qnt"],
                    "price": i["price"],
                    "action": i["action"],
                    "avg": i["avg"],
                    "p_l": i["p_l"]
                }})
    return formateddata


@api_view()
def get_data(request):
    param1 = request.GET.get('id')
    if param1=="all" or param1==None:
        trade_obj = Trade.objects.all()
        serializer = TradeSerialize(trade_obj, many=True)
        # print(serializer.data[1]["uuid"])
        return Response({
            'status': True,
            'message': 'fetch data  ',
            'open': formatedData(serializer.data)
        })
    else:
        print(param1)
        try:
            open_data = Trade.objects.get(pk=param1)
            serializer = TradeSerialize(open_data)
            return Response({
                'status': True,
                'message': 'fetch data  ',
                'open': formatedData(serializer.data)

            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error ',

            }, status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_by_id(request, pk):
    try:
        open_data = Trade.objects.get(pk=pk)
        data = open_data.delete()

        return Response({
            'status': True,
            'message': 'deleted ',
            'data': data
        })
    except Exception:
        return Response({
            'status': False,
            'message': 'Error ',
        })


@api_view()
# def get_by_id(request, pk):
#     try:
#         print(pk)
#         open_data = Trade.objects.get(pk=pk)
#         serializer = TradeSerialize(open_data)
#         return Response({
#             'status': True,
#             'message': 'fetch data  ',
#             'open': formatedData(serializer.data)
#
#         }, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({
#             'status': False,
#             'message': 'Error ',
#
#         }, status=status.HTTP_404_NOT_FOUND)
#

@api_view(['PATCH'])
def update_by_id(request, pk):
    try:
        open_data = Trade.objects.get(pk=pk)
    except Trade.DoesNotExist:
        return Response({
            'status': False,
            'message': 'Error ',
        })

    serializer = TradeSerialize(open_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


def add_data(data, pk):
    open_data = Trade.objects.get(pk=pk)
    serializer = TradeSerialize(open_data, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


def is_exist(name, new_data):
    try:
        print(name)
        open_data = Trade.objects.get(name=name)
        serializer = TradeSerialize(open_data)
        old_data = serializer.data
        if new_data["action"] == "buy":
            avg = ((old_data['qnt'] * old_data['price']) + (new_data['qnt'] * new_data['price'])) / (
                        old_data['qnt'] + new_data['qnt'])
            p_l = (old_data['qnt'] - new_data['qnt']) * avg
            add_data(pk=old_data["uuid"],
                     data={"name": name, "price": new_data["price"], "action": new_data["action"], "avg": avg,
                           "p_l": p_l, "qnt": new_data["qnt"] + old_data["qnt"]})
        else:
            avg = ((old_data['qnt'] * old_data['price']) + (new_data['qnt'] * new_data['price'])) / (
                    old_data['qnt'] + new_data['qnt'])
            p_l = (old_data['qnt'] - new_data['qnt']) * avg
            add_data(pk=old_data["uuid"],
                     data={"name": name, "price": new_data["price"], "action": new_data["action"], "avg": avg,
                           "p_l": p_l, "qnt": new_data["qnt"] - old_data["qnt"]})

        print(avg, p_l)
        return True
    except Exception as e:
        print(e)
        serializer=TradeSerialize(data=new_data)
        if serializer.is_valid():
            serializer.save()
        return False



@api_view(['POST'])
def post_data(request):
    try:
        data = request.data
        serializer = TradeSerialize(data=data)
        if serializer.is_valid():
            is_exist(serializer.data["name"], serializer.data)

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
class Trade_view(APIView):
    def get(self,request):
        param1 = request.GET.get('id')
        if param1 == "all" or param1 == None:
            trade_obj = Trade.objects.all()
            serializer = TradeSerialize(trade_obj, many=True)
            # print(serializer.data[1]["uuid"])
            return Response({
                'status': True,
                'message': 'fetch data  ',
                'open': formatedData(serializer.data)
            })
        else:
            print(param1)
            try:
                open_data = Trade.objects.get(pk=param1)
                serializer = TradeSerialize(open_data)
                return Response({
                    'status': True,
                    'message': 'fetch data  ',
                    'open': formatedData(serializer.data)

                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    'status': False,
                    'message': 'Error ',

                }, status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        try:
            data = request.data
            serializer = TradeSerialize(data=data)
            if serializer.is_valid():
                is_exist(serializer.data["name"], serializer.data)

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

    def patch(self,request):
        param1 = request.GET.get('id')
        try:
            open_data = Trade.objects.get(pk=param1)
        except Trade.DoesNotExist:
            return Response({
                'status': False,
                'message': 'Error ',
            })

        serializer = TradeSerialize(open_data, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request):
        param1 = request.GET.get('id')
        try:
            open_data = Trade.objects.get(pk=param1)
            data = open_data.delete()

            return Response({
                'status': True,
                'message': 'deleted ',
                'data': data
            })
        except Exception:
            return Response({
                'status': False,
                'message': 'Error ',
            })