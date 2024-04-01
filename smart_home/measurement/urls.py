from django.urls import path
from .views import AddSensorView, SensorView, ChangeSensorView, AddMeasurementsView

urlpatterns = [
    path('AddSensor/', AddSensorView.as_view()),
    path('AddMeasurements/', AddMeasurementsView.as_view()),
    path('ChangeSensor/', ChangeSensorView.as_view()),
    path('sensor/', SensorView.as_view()),
    path('sensor/<int:pk>/', SensorView.as_view()),
]

