from django.contrib import admin
from pays.models import Pay

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    pass