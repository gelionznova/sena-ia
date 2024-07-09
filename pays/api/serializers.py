from rest_framework.serializers import ModelSerializer
from pays.models import Pay


class PaySerializer(ModelSerializer):
    class Meta:
        model = Pay
        fields = ["id","pay_money","created_at"]