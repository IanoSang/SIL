from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import ImageSerializer
from .models import Image


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        photo = request.data['photo']
        photo_name = request.data['photo_name']
        Image.objects.create(photo_name=photo_name, photo=photo)
        return HttpResponse({'message': 'Photo uploaded'}, status=200)
