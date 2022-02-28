from rest_framework import serializers

from core.models import Upupa

class UpupaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upupa
        fields = ['uuid', 'message', 'extra', 'created_at']