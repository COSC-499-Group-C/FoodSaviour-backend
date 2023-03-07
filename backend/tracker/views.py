from .models import WasteType, TrackerData
from .serializers import WasteTypeSerializer, TrackerDataSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication


class WasteTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Waste Type to be viewed or edited.
    """
    authentication_classes = [SessionAuthentication, ]
    queryset = WasteType.objects.all()
    serializer_class = WasteTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrackerDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tracker Data to be viewed or edited
    """
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    queryset = TrackerData.objects.all()
    serializer_class = TrackerDataSerializer
    permission_classes = [permissions.IsAuthenticated]
