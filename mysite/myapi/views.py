from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializer import DeviceSerializer, MedHistorySerializer, UserSerializer
from .models import Device, MedHistory, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('lastName')
    serializer_class = UserSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('deviceSKU')
    serializer_class = DeviceSerializer

class MedHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedHistory.objects.all().order_by('uid')
    serializer_class = MedHistorySerializer