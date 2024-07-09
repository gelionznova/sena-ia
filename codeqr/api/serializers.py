from rest_framework.serializers import ModelSerializer
from codeqr.models import Codeqr


class CodeqrSerializer(ModelSerializer):
    class Meta:
        model = Codeqr
        fields = ["id", "number_ticket", "number_one", "number_two"]
