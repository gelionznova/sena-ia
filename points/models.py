from django.db import models
from django.utils import timezone 

StatusEnum = (
    ("MASCULINO", "masculino"), 
    ("FEMENINO", "femenino"), 
    ("OTRO", "otro")
)

class Point(models.Model):
    pack = models.CharField(max_length=50, blank=True, null=True, default="")
    salesperson = models.CharField(max_length=50, blank=True, null=True, default="")
    first_name = models.CharField(max_length=50, blank=True, null=True, default="")
    last_name = models.CharField(max_length=50, blank=True, null=True, default="")
    id_number = models.CharField(max_length=20, blank=True, null=True, default="")
    gender = models.CharField(max_length=50, choices=StatusEnum, blank=True, null=True, default="")
    email = models.EmailField(blank=True, null=True, default=" ")
    phone_number = models.CharField(max_length=20, blank=True, null=True, default="")
    address = models.CharField(max_length=100, blank=True, null=True, default="")
    pay_money = models.CharField(max_length=20, blank=True, null=True, default="")
    validate_ticket = models.CharField(max_length=20, blank=True, null=True, default="", unique=True)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.validate_ticket
