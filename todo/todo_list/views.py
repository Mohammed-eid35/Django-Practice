import imp
from django.shortcuts import render
from rest_framework import generics

from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.

class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
