from django.db import models
import uuid

class Device(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    description = models.CharField(max_length=150, default='')

class Coordinate(models.Model):
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    

