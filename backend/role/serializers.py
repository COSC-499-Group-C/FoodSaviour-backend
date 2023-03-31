from rest_framework import serializers
from .models import RoleName, RoleGroup


class RoleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleName
        fields = [
            "id",
            "name"
        ]

        
class RoleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleGroup
        fields = [
            "id",
            "group",
            "user"
        ]
