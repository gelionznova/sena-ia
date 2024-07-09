from django.contrib import admin

from codeqr.models import Codeqr

@admin.register(Codeqr)
class CodeqrAdmin(admin.ModelAdmin):
    pass