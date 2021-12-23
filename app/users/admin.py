from django.contrib import admin

from rest_framework_api_key.admin import APIKeyModelAdmin

from users.models import Organization, OrganizationAPIKey


@admin.register(OrganizationAPIKey)
class OrganizationAPIKeyModelAdmin(APIKeyModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "created_at", "updated_at"]
    list_display = [
        "user",
        "name",
        "slug",
        "created_at",
    ]
    list_filter = []
