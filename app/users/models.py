from django.db import models
from django.contrib.auth.models import User

from rest_framework_api_key.models import AbstractAPIKey
from shortuuid.django_fields import ShortUUIDField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from hoopoe.utils import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    image = models.ImageField(
        upload_to="photos/users/profiles/%y/%m/%d/", blank=True, null=True
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFit(width=100, upscale=False)],
        format="JPEG",
        options={"quality": 60},
    )

    metadata = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username


class Organization(models.Model):
    uuid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="organizations"
    )
    name = models.CharField(max_length=128, blank=True, null=True)
    slug = models.CharField(max_length=128, blank=True, null=True)
    active = models.BooleanField(default=True)
    is_personal = models.BooleanField(
        default=False, help_text="Is this a personal organization?"
    )

    image = models.ImageField(
        upload_to="photos/users/organizations/%y/%m/%d/", blank=True, null=True
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFit(width=100, upscale=False)],
        format="JPEG",
        options={"quality": 60},
    )

    metadata = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)


class OrganizationAPIKey(AbstractAPIKey):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )


class Recipient(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="recipients",
    )
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

    image = models.ImageField(
        upload_to="photos/users/recipients/%y/%m/%d/", blank=True, null=True
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFit(width=100, upscale=False)],
        format="JPEG",
        options={"quality": 60},
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("organization", "username")


class Driver(models.Model):
    EMAIL = 0
    TELEGRAM = 1

    TYPES = [
        (EMAIL, "EMAIL"),
        (TELEGRAM, "TELEGRAM"),
    ]

    recipient = models.ForeignKey(
        Recipient,
        on_delete=models.CASCADE,
        related_name="drivers",
    )
    type = models.IntegerField(choices=TYPES, default=0)
    account_id = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_id
