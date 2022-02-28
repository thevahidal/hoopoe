from django.db import models

from shortuuid.django_fields import ShortUUIDField

from users.models import Organization

class Upupa(models.Model):
    uuid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="",
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="upupas"
    )
    message = models.TextField(null=True, blank=True)
    extra = models.JSONField(default=dict)

    metadata = models.JSONField(default=dict)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
