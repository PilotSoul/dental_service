from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
import uuid
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Image

# Create your views here.
from .serializers import DentalDetectionSerializer


# class DentalDetectionAPIView(generics.ListAPIView):
#     queryset = Image.objects.all()
#     serializer_class = DentalDetectionSerializer

class DentalDetectionAPIView(APIView):
    def get(self, request):
        lst = Image.objects.all().values()
        return Response({'images': list(lst)})

    def post(self, request):
        new_uuid = str(uuid.uuid4())[:7]
        image_new = Image.objects.create(
            name=str(request.data['photo'])+new_uuid,
            photo=request.data['photo']
        )
        return Response('ok')