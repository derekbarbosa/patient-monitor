# serializers.py

from rest_framework import serializers

from .models import Device, MedHistory, User

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
    