from rest_framework import serializers
class EntitySerializer(serializers.Serializer):
    pass
    ip = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    timestamp = serializers.DateTimeField()
    location = serializers.CharField(max_length=255)
    device_info = serializers.CharField(max_length=255)