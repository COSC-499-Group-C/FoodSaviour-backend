from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import OrgName, OrgGroup
from .serializers import OrgNameSerializer, OrgGroupSerializer

from django.shortcuts import get_object_or_404


# OrgName api views

# List all organizations
class OrganizationListCreateApiView(generics.ListCreateAPIView):
    queryset = OrgName.objects.all()
    serializer_class = OrgNameSerializer

    def perform_create(self, serializer):
        serializer.save()


organization_list_create_view = OrganizationListCreateApiView.as_view()


# Provide details for 1 particular organization
class OrganizationDetailApiView(generics.RetrieveAPIView):
    queryset = OrgName.objects.all()
    serializer_class = OrgNameSerializer


organization_detail_view = OrganizationDetailApiView.as_view()


# Update the fields for 1 Organizations
class OrganizationUpdateApiView(generics.UpdateAPIView):
    queryset = OrgName.objects.all()
    serializer_class = OrgNameSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


organization_update_view = OrganizationUpdateApiView.as_view()


# Delete/Destroy organization
class OrganizationDeleteApiView(generics.DestroyAPIView):
    queryset = OrgName.objects.all()
    serializer_class = OrgNameSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # any changes with instance here
        super().perform_destroy(instance)


organization_delete_view = OrganizationDeleteApiView.as_view()


# Alternative way to do List and create organization - Might want to use for complex API in future
@api_view(['GET', 'POST'])
def organization_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # list one organization
        if pk is not None:
            obj = get_object_or_404(OrgName, pk=pk)
            data = OrgNameSerializer(obj, many=False).data
            return Response(data)

        # list all organizations
        queryset = OrgName.objects.all()
        data = OrgNameSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an organization
        serializer = OrgNameSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response({"invalid": "invalid data"}, status=400)


# OrgGroup API views
# List all Org Groups
class OrgGroupListCreateApiView(generics.ListCreateAPIView):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        if not instance.user_id:
            instance.user_id = self.request.user.id


org_group_list_create_view = OrgGroupListCreateApiView.as_view()


# Provide details for 1 particular Org Group
class OrgGroupDetailApiView(generics.RetrieveAPIView):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer


org_group_detail_view = OrgGroupDetailApiView.as_view()


# Update the fields for 1 Organizations
class OrgGroupUpdateApiView(generics.UpdateAPIView):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


org_group_update_view = OrgGroupUpdateApiView.as_view()


# Delete/Destroy organization
class OrgGroupDeleteApiView(generics.DestroyAPIView):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # any changes with instance here
        super().perform_destroy(instance)


org_group_delete_view = OrgGroupDeleteApiView.as_view()
