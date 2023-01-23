from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import ImageSerializer
from .models import Image
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        photo = request.data['photo']
        photo_name = request.data['photo_name']
        Image.objects.create(photo_name=photo_name, photo=photo)
        return HttpResponse({'message': 'Photo uploaded'}, status=200)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
