from django.db import models
from django.contrib.auth.models import User

from rest_framework_api_key.models import AbstractAPIKey
from shortuuid.django_fields import ShortUUIDField

from hoopoe.utils import slugify


class Organization(models.Model):
    uuid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organizations"
    )
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)
        

class OrganizationAPIKey(AbstractAPIKey):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )
    
    