from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from pays.models import Pay
from pays.api.serializers import PaySerializer


class PayApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    