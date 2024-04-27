from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_url ={
        'list':'/task-list/',
        'Detail view':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update<str:pk>/',
        'Delete':'/task-delete<str:pk>/',

    }
@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer= TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer= TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer= TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer= TaskSerializer(tasks, many=False)
    tt=serializer
    tasks.delete()  
    

    return Response(tt.data)

@api_view(['PUT'])
def taskupdate(request,pk):
    tasks = Task.objects.get(id=pk)

    serializer= TaskSerializer(tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

    