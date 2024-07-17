from rest_framework.serializers import ModelSerializer
from points.models import Point
from codeqr.api.serializers import CodeqrSerializer

class PointSerializer(ModelSerializer):
    
    class Meta:
        model = Point
        fields = [
            "id",
            "pack",
            "salesperson",
            "first_name",
            "last_name",
            "id_number",
            "gender",
            "email",
            "phone_number",
            "address",            
            "pay_money",
            "validate_ticket",
            "created_at",                       
        ]