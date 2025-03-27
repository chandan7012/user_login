from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from user.authentication import CustomJWTAuthentication
from .services import create_task, get_task, update_task, delete_task

class Task(APIView):
    authentication_classes = [CustomJWTAuthentication]
    
    def get(self, request):
        response, status = get_task(request)
        return Response(data=response, status=status)
    
    def post(self, request):
        response, status = create_task(request)
        return Response(data=response, status=status)

class TaskDetails(APIView):
    authentication_classes = [CustomJWTAuthentication]
    
    def get(self, request, id):
        response, status = get_task(request = request, task_id = id)
        return Response(data=response, status=status)

    def put(self, request, id):
        response, status = update_task(request = request, task_id = id)
        return Response(data=response, status=status)

    def delete(self, request, id):
        response, status = delete_task(request = request, task_id = id)
        return Response(data=response, status=status)