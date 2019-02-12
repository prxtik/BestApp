from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .functions import Bus
# Create your views here.


@api_view(['POST'])
def Addlocation(request):
    if request.method=='POST':
        data = request.data
        bus = Bus()
        bus.addDataInQueue(data)
        return Response(status= status.HTTP_200_OK)

@api_view(['GET'])
def GetLocationVal(request):
    if request.method=='GET':
        bus = Bus()
        loc = bus.popDatafromQueue()
        return Response(loc)



    