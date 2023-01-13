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
    group_id = OrgNameSerializer()

    class Meta:
        model = OrgGroup
        fields = [
            "id",
            "group_id",
            "user_id"
        ]