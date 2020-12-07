import json

import requests
from django.core import serializers
from rest_framework import generics, permissions
from rest_framework.response import Response

from interview.secrets import API_KEY

from .serializers import *


class LocationViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = LocationSerializer

    def post(self, request, *args, **kwargs):
        base_url = "http://api.ipstack.com/"
        data = {}
        if self.request.query_params.get("url"):
            url_to_check = self.request.query_params.get("url")
            try:
                location_by_url = Location.objects.filter(
                    url=url_to_check).values()[0]
                return Response({"location": location_by_url})
            except IndexError:
                pass
            res = requests.get(
                f"{base_url}{url_to_check}?access_key={API_KEY}")
            data["url"] = url_to_check
        elif self.request.query_params.get("ip"):
            ip = self.request.query_params.get("ip")
            try:
                location_by_ip = Location.objects.filter(
                    url=url_to_check).values()[0]
                return Response({"location": location_by_ip})
            except IndexError:
                pass
            res = requests.get(f"{base_url}{ip}?access_key={API_KEY}")

        data.update(res.json())
        ip_type = data.pop("type")
        location = data.pop("location")
        data["ip_type"] = ip_type
        data.update(location)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        location = serializer.save()
        return Response({"location": serializer.data})
