from django.db import models
from django.contrib.auth.models import User

class BlockedCall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    call_date = models.DateField()
    call_time = models.TimeField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location_name = models.CharField(max_length=255)
    block_reason = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.phone_number} - {self.call_date}"
