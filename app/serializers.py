from rest_framework import serializers
from .models import Image, File


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['photo', 'photo_name', 'date', 'album']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
