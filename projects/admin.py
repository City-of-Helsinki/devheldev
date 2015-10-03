from django.contrib import admin
from .models import Project, ProjectLink


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
