from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializer import AllergiesSerializer, DeviceSerializer, MeasurementSerializer, MeasurementsSerializer, MedHistorySerializer, OperationSerializer, UserSerializer
from .models import Allergies, Medications, Measurements, Measurement, Operation, Device, MedHistory, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('lastName')
    serializer_class = UserSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('deviceSKU')
    serializer_class = DeviceSerializer


class MedHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedHistory.objects.all().order_by('uid')
    serializer_class = MedHistorySerializer


class AllergiesViewSet(viewsets.ModelViewSet):
    queryset = Allergies.objects.all().order_by('medhistory')
    serializer_class = AllergiesSerializer


class MedicationsViewset(viewsets.ModelViewSet):
    queryset = Medications.objects.all().order_by('medhistory')
    serializer_class = MedHistorySerializer

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all().order_by('medhistory')
    serializer_class = OperationSerializer

class MeasurementsViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all().order_by('medhistory')
    serializer_class = MeasurementsSerializer

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all().order_by('measurements')
    serializer_class = MeasurementSerializer