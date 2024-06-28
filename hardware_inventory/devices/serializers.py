# devices/serializers.py
from rest_framework import serializers
from .models import Device, NetworkPort

class NetworkPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkPort
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    ports = NetworkPortSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'