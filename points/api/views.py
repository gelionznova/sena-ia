from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.exceptions import ValidationError
from django.db import IntegrityError

from points.models import Point
from points.api.serializers import PointSerializer

class PointApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PointSerializer
    queryset = Point.objects.all()
    filter_backends= [DjangoFilterBackend]
    filter_fields= [ "validate_ticket"]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            raise ValidationError({"detail": "Este registro ya existe. Verifica los campos únicos."})
