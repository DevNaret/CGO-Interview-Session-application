from django.shortcuts import render
from rest_framework import status
# from rest_framework import viewsets
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from rest_framework.renderers import JSONRenderer
from CGO_Interview_Session.models import Frog
from CGO_Interview_Session.modelsSerializers import FrogSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.schemas import AutoSchema


# Create your views here.
# class solution

def get_time(data):
    for i in range (len(data['A'])):
        if data['A'][i] == data['X']:
            return i
    return -1



@api_view(['GET'])
def solution(request):
    """
    X is last position on the falling leaves

    A are position where one leaf falls at time 

    return K for time (sec)
    """
    # print(request)

    data = JSONParser().parse(request)
    frog_serializer = FrogSerializer(data=data)
    if frog_serializer.is_valid():
        _k_time_sec = get_time(frog_serializer.data)
        return Response(_k_time_sec, status=200)
    else:
        return JsonResponse(frog_serializer.errors, status=204)
    