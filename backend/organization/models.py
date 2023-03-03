from django.db import models
from user.models import NewUser


class OrgName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "OrgNames"


class OrgGroup(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    group = models.ForeignKey(OrgName, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "OrgGroups"
        unique_together = ["user", "group"]

