from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from api import serializers
# above 'serializer' represents folder name and '.' in front of 'serializer' tells that it belongs to the same folder 

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    # this view will show us all the url patterns we have
    # 'put' method is similar to 'update' method
    api_urls = {
        'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
    }
    # the 'Response' will render out the data in the json format 
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all() # we are getting all the tags from here
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk) # we are getting one specific tag from here
    serializer = TaskSerializer(tasks, many=False)
    # the above 'many=false' funtion is used to get one specific task
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer( instance=task , data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item successfully Deleted !!!')