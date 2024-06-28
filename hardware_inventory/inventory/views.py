from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import HardwareItem
from .serializers import HardwareItemSerializer
from hardware_inventory.json_renderer import CustomJSONRenderer
from .filters import HardwareItemFilter

class HardwareItemViewSet(viewsets.ModelViewSet):
    queryset = HardwareItem.objects.all()
    serializer_class = HardwareItemSerializer
    renderer_classes = [CustomJSONRenderer]
    filterset_class = HardwareItemFilter
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'items': serializer.data})

        serializer = self.get_serializer(queryset, many=True)
        return Response({'items': serializer.data})
    
    @action(detail=True, methods=['patch'])
    def update_status(self,request,pk=None):
        item = self.get_object()
        status = request.data.get('status')
        if status and status in dict(HardwareItem.status_choices):
            item.status = status
            item.save()
            return Response({'status': item.status})
        return Response({'status':'Invalid status'},status=400)