from django.urls import path, include
from rest_framework import routers

from user.views import UserViewSet
from organization.views import OrgNameViewSet, OrgGroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orgName', OrgNameViewSet)
router.register(r'orgGroup', OrgGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),  # https://localhost:8000/
]
