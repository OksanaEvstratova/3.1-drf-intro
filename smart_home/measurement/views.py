from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorListSerializer
from .models import Sensor, Measurement


class AddSensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': serializer.data})
        else:
            return Response(serializer.errors)


class ChangeSensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.update(Sensor.objects.get(name=request.data['name']), request.data)
            return Response({'status': serializer.data})
        else:
            return Response(serializer.errors)


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get(self, request, pk=0):
        if pk == 0:
            self.serializer_class = SensorListSerializer
            sensors = Sensor.objects.all()
        else:
            try:
                sensors = Sensor.objects.get(id=pk)
            except Sensor.DoesNotExist:
                return Response({'error': 'DoesNotExist'})

        return Response(self.serializer_class(sensors, many=pk == 0).data)


class AddMeasurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': serializer.data})
        else:
            return Response(serializer.errors)

