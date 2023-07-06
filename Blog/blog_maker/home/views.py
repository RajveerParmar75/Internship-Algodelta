from pprint import pprint
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Layout, Header, ContentData
from .serializer import MainDataSerializer, HeaderDataSerializer, ContentDataSerializer


class MainDataView(APIView):

    def get(self, request):
        dat = Layout.objects.all().values()
        pprint(dat)
        serializer = MainDataSerializer(data=list(dat), many=True)
        serializer.is_valid(raise_exception=True)
        return Response({
            "status": 200,
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = MainDataSerializer(data=data)
        if serializer.is_valid():
            ins = serializer.save()
            print(ins)
            return Response({
                "status": 200,
                "message": "data is added",
                "data": serializer.data
            })
        else:

            return Response({
                "status": 400,
                "message": "error",
                "data": serializer.errors
            })
    def delete(self, request):
        data = request.data
        try:
            record = Layout.objects.get(id=data['id'])
            record.delete()
            return Response({
                "status":True,
                "message":"data is deleted"
            })
        except Layout.DoesNotExist:
            return Response({
                "status":False,
                "message":"does not exist"
            })

class HeaderView(APIView):
    def get(self, request):
        dat = Header.objects.all().values()
        pprint(dat)
        serializer = HeaderDataSerializer(data=list(dat), many=True)
        serializer.is_valid(raise_exception=True)
        return Response({
            "status": 200,
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = HeaderDataSerializer(data=data)
        if serializer.is_valid():
            ins = serializer.save()
            print(ins)
            return Response({
                "status": 200,
                "message": "data is added",
                "data": serializer.data
            })
        else:
            return Response({
                "status": 400,
                "message": "error",
                "data": serializer.errors
            })


class ContentView(APIView):
    def get(self, request):
        dat = ContentData.objects.all().values()
        pprint(dat)
        serializer = ContentDataSerializer(data=list(dat), many=True)
        serializer.is_valid(raise_exception=True)
        return Response({
            "status": 200,
            "data": serializer.data
        })
    def replace_value(self, html, data):
        string=""
        for i in range(len(data)):
            string+=str(html[i]).format(title=data[i]['title'],img=data[i]['image'],content=data[i]['text'])
        return string
    def post(self, request):
        data = request.data
        serializer = ContentDataSerializer(data=data, many=True)
        if serializer.is_valid():
            html_list = []
            for i in serializer.data:
                html_list.append(Layout.objects.get(id=i['layout_id']).html)

            return Response({
                "status": 200,
                "message": "valid",
                "data": self.replace_value(html=html_list,data=serializer.data)
            })
            # layout = Layout.objects.all(id=data['layout_id'])
            # replacement={
            #     "**img**":data['image'],
            #     "**text**": data['text'],
            #     "**title**": data['title'],
            # }
            # send_data= self.replace_value(layout['html'],replacement)
            # return Response({
            #     "status": 200,
            #     "message": "data is added",
            #     "data": send_data
            # })
        else:
            return Response({
                "status": 400,
                "message": "error",
                "data": serializer.errors
            })
