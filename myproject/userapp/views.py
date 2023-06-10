from django.shortcuts import render
from .models import UserData
from .serializer import Dataserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class StudentreadModelViewset(viewsets.ReadOnlyModelViewSet):
   queryset = UserData.objects.all()
   serializer_class = Dataserializer