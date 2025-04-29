from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'user', 'file_name', 'file_url']
        read_only_fields = ['user', 'file_url']
