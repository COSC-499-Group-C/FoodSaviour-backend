from .models import WasteType, TrackerData
from .serializers import WasteTypeSerializer, TrackerDataSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django_filters import rest_framework as filters


class WasteTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Waste Type to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
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
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('waste_type',)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user_id=user.id).order_by('-created_at')
