from django.contrib import admin

from rest_framework_api_key.admin import APIKeyModelAdmin

from users.models import Driver, Organization, OrganizationAPIKey, Recipient


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


@admin.register(Recipient)
class RecipientTypeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "name",
        "organization",
        "active",
        "created_at",
    ]
    list_filter = []


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "recipient",
        "organization",
        "type",
        "username",
        "active",
        "created_at",
    ]
    list_filter = []
    
    def organization(self, obj):
        return obj.recipient.organization
