from django.urls import path, include
from rest_framework import routers

from user.views import UserViewSet
from organization.views import OrgNameViewSet, OrgGroupViewSet
from tracker.views import WasteTypeViewSet, TrackerDataViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orgName', OrgNameViewSet)
router.register(r'orgGroup', OrgGroupViewSet)
router.register(r'wasteType', WasteTypeViewSet)
router.register(r'trackerData', TrackerDataViewSet)

urlpatterns = [
    path('', include(router.urls)),  # https://localhost:8000/
]
