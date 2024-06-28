# devices/models.py
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    mac_address = models.CharField(max_length=17)
    device_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    firmware_version = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class NetworkPort(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='ports')
    port_number = models.CharField(max_length=10)
    speed = models.CharField(max_length=50)
    vlan = models.CharField(max_length=50)
    connected_device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, blank=True, related_name='connected_ports')

    def __str__(self):
        return f"{self.device.name} - Port {self.port_number}"
