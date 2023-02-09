from rest_framework import serializers

from .models import WasteType, TrackerData


class WasteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteType
        fields = [
            "id",
            "name"
        ]


class TrackerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackerData
        fields = [
            "id",
            "description",
            "data",
            "waste_type",
            "user"
        ]
