from django.contrib import admin
from points.models import Point

@admin.register(Point)
class pointAdmin(admin.ModelAdmin):
    pass
