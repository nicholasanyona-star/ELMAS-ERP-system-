# Role-Based Access Control

# This file implements role-based access control for the Django admin.

from django.contrib import admin
from django.contrib.auth.models import Group, Permission

class RoleBasedAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        role = request.user.groups.first()  # Assuming user belongs to a single group
        # Filter queryset based on role
        if role:
            return qs.filter(role=role)
        return qs

# Register your admin classes here
