from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
import io
from PIL import Image as im
from .image_recognition import *

from .models import Image


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
        uploaded_img = Image.objects.filter().last()
        img_bytes = uploaded_img.photo.read()
        img = im.open(io.BytesIO(img_bytes))
        result = detect_teeth_with_yolo(img)
        print(result)

        return Response('ok')