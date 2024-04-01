from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.CharField(max_length=50, verbose_name='Описание')

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date_time = models.DateTimeField(auto_now=True)
