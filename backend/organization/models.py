from django.db import models
from django.contrib.auth.models import User


class OrgName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "OrgNames"


class OrgGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(OrgName, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "OrgGroups"
        unique_together = ["user", "group"]

