from .models import OrgName, OrgGroup
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import OrgNameSerializer, OrgGroupSerializer


class OrgNameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Organization names to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    queryset = OrgName.objects.all()
    serializer_class = OrgNameSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OrgGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Organization Group relation to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
