from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from organization.models import OrgName
from organization.serializers import OrgNameSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = OrgName.objects.all()
    data = {"data": []}
    if instance:
        for query in instance:
            data["data"].append(OrgNameSerializer(query).data)
    return Response(data)
