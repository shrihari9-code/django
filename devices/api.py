# devices/api.py
from rest_framework import serializers, viewsets
from .models import Device
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'description', 'modified'] 

class DeviceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('modified',) 

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceUpdateAPIView(APIView):
    def post(self, request, device_id):
        device = Device.objects.get(pk=device_id)
        serializer = DeviceUpdateSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
