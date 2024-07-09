
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from codeqr.models import Codeqr
from codeqr.api.serializers import CodeqrSerializer

class CodeqrApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CodeqrSerializer
    queryset = Codeqr.objects.all()

    

    

    

    