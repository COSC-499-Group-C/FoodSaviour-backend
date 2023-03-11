
from django_filters import rest_framework as filters
from django.db.models import Q
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import WasteType, TrackerData
from organization.views import OrgGroup
from .serializers import WasteTypeSerializer, TrackerDataSerializer


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


class CustomTrackerData(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # data = TrackerData.objects.filter(id__in=[2, 3])
        waste_ids = self.request.query_params.getlist('waste_type')
        org_ids = self.request.query_params.getlist('group')

        org_data = OrgGroup.objects.filter(group__id__in=org_ids)

        user_list = []
        for org in org_data:
            user_list.append(org.user.id)

        if not waste_ids and not org_data:
            tracker_data = TrackerData.objects.all()
        elif waste_ids and org_data:
            tracker_data = TrackerData.objects.filter(user__id__in=user_list, waste_type__id__in=waste_ids)
        elif not waste_ids:
            tracker_data = TrackerData.objects.filter(user__id__in=user_list)
        elif not org_data:
            tracker_data = TrackerData.objects.filter(waste_type__id__in=waste_ids)

        serialized = TrackerDataSerializer(tracker_data, many=True)
        return Response(serialized.data)
