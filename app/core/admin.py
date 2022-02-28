from django.contrib import admin

from core.models import Upupa


@admin.register(Upupa)
class UpupaAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = [
        "organization",
        "message",
        "created_at",
    ]
    list_filter = [
        "organization",
    ]
