from django.urls import path, include
from rest_framework import routers

from user.views import UserViewSet
from organization.views import OrgNameViewSet, OrgGroupViewSet
from tracker.views import WasteTypeViewSet, TrackerDataViewSet, CustomTrackerData
from user.views import CustomUserCreate, BlacklistTokenUpdateView
from role.views import RoleNameViewSet, RoleGroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orgName', OrgNameViewSet)
router.register(r'orgGroup', OrgGroupViewSet)
router.register(r'roleName', RoleNameViewSet)
router.register(r'roleGroup', RoleGroupViewSet)
router.register(r'wasteType', WasteTypeViewSet)
router.register(r'trackerData', TrackerDataViewSet)
router.register(r'filteredTrackerData', CustomTrackerData, basename="filtered_Tracker_Data")
router.register(r'register', CustomUserCreate, basename="register_user")
router.register(r'logout/blacklist', BlacklistTokenUpdateView, basename="blacklist_token")

urlpatterns = [
    path('', include(router.urls)),  # https://localhost:8000/
]
