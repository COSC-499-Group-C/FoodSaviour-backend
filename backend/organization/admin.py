from django.contrib import admin
from .models import OrgName, OrgGroup


admin.site.register(OrgGroup)
admin.site.register(OrgName)
