from django.db import models
from user.models import NewUser
from django.utils import timezone


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
    description = models.CharField(max_length=150, default="Description")
    waste_type = models.ForeignKey(WasteType, on_delete=models.CASCADE, null=False)
    donations = models.DecimalField(max_digits=10, decimal_places=5)
    compost = models.DecimalField(max_digits=10, decimal_places=5)
    partners = models.DecimalField(max_digits=10, decimal_places=5)
    farmers = models.DecimalField(max_digits=10, decimal_places=5)
    gardens = models.DecimalField(max_digits=10, decimal_places=5)
    landfill = models.DecimalField(max_digits=10, decimal_places=5)
    other = models.DecimalField(max_digits=10, decimal_places=5)
    created_at = models.DateTimeField(default=timezone.localtime(timezone.now()))
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Tracker Data"
