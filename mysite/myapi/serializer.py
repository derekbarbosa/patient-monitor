# serializers.py

from dataclasses import fields
from rest_framework import serializers

from .models import Operation, Measurements, Measurement, Medications, Allergies, Device, MedHistory, User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'id')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Device
        fields = ('deviceSKU', 'did', 'uid')


class MedHistorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MedHistory
        fields = ('uid')


class AllergiesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Allergies
        fields = ('medhistory', 'allergy', 'severity')


class MedicationsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Medications
        fields = ('medhistory', 'medId', 'isValid', 'prescribedBy')


class OperationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Operation
        fields = ('medhistory', 'performedBy', 'type')


class MeasurementsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Measurements
        fields = ('medhistory', 'uid', 'did', 'time')


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Measurement
        fields = ('measurements', 'height', 'weight', 'BMI', 'bloodPressure',
                  'bloodO2', 'heartRate', 'temperature')
