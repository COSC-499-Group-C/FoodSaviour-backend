from .models import RoleName, RoleGroup
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RoleNameSerializer, RoleGroupSerializer


class RoleNameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Role names to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    queryset = RoleName.objects.all()
    serializer_class = RoleNameSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RoleGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Role Group relation to be viewed or edited.
    """

    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    queryset = RoleGroup.objects.all()
    serializer_class = RoleGroupSerializer
    # permission_classes = [permissions.IsAuthenticated]