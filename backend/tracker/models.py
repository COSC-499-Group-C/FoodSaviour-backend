from django.db import models
from django.contrib.auth.models import User


class WasteType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Waste Types"


def tracker_data_default():
    return {
        "data": {
            "data-point-1": "example 1",
            "data-point-2": "example 2"
        }
    }


class TrackerData(models.Model):
    description = models.CharField(max_length=500, default="Description")
    waste_type = models.ForeignKey(WasteType, on_delete=models.CASCADE, null=False)
    data = models.JSONField("Tracker Data", default=tracker_data_default)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tracker Data"
