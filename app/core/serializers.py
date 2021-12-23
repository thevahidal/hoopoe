from rest_framework import serializers

class UpupaSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200, required=True)
    extra = serializers.DictField(required=False)