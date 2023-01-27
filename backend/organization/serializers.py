from rest_framework import serializers

from .models import OrgName, OrgGroup


class OrgNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgName
        fields = [
            "id",
            "name"
        ]


class OrgGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgGroup
        fields = [
            "id",
            "group",
            "user"
        ]