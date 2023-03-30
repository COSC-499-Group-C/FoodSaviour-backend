from django.contrib import admin
from .models import RoleName, RoleGroup

admin.site.register(RoleGroup)
admin.site.register(RoleName)