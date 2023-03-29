from django.db import models
from user.models import NewUser


class RoleName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "RoleNames"


class RoleGroup(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    group = models.ForeignKey(RoleName, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "RoleGroups"
        unique_together = ["user", "group"]
