from rest_framework import viewsets
from .models import Device, NetworkPort
from .serializers import DeviceSerializer, NetworkPortSerializer
import requests
from django.http import JsonResponse
from rest_framework.views import APIView

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class NetworkPortViewSet(viewsets.ModelViewSet):
    queryset = NetworkPort.objects.all()
    serializer_class = NetworkPortSerializer

class GNS3ProjectAPIView(APIView):
    def get(self, request):
        url = 'http://localhost:3080/v2/projects'
        username = 'admin'
        password = 'Lr8E4MVaqZsigYxU4zfFgtPLm1E9gmgfkx2TyObQqYKJHRHGgRYQLGp3WKJGyNWr'
        response = requests.get(url, auth=(username, password))
        
        try:
            response.raise_for_status()  # Check for any HTTP errors
            json_data = response.json()
            return JsonResponse(json_data, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)

    def post(self, request):
        url = 'http://localhost:3080/v2/projects'
        username = 'admin'
        password = 'Lr8E4MVaqZsigYxU4zfFgtPLm1E9gmgfkx2TyObQqYKJHRHGgRYQLGp3WKJGyNWr'
        project_data = {
            "name": request.data.get("name"),
            "project_id": request.data.get("project_id")
        }
        response = requests.post(url, json=project_data, auth=(username, password))
        
        try:
            response.raise_for_status()  # Check for any HTTP errors
            json_data = response.json()
            return JsonResponse(json_data, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
