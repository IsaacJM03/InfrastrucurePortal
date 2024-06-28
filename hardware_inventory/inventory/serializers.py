from rest_framework import serializers
from .models import HardwareItem

class HardwareItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardwareItem
        fields = '__all__'
        read_only_fields = ['status_history']
