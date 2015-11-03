from django.contrib import admin
from .models import ProjectRoleType


@admin.register(ProjectRoleType)
class ProjectRoleTypeAdmin(admin.ModelAdmin):
    pass
