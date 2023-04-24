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
        uploaded_img = Image.objects.create(
            name=str(request.data['photo'])+new_uuid,
            photo=request.data['photo']
        )
        # uploaded_img = Image.objects.filter().last()
        path_to_image = str(uploaded_img.photo)
        # img_bytes = uploaded_img.photo.read()
        # img = im.open(io.BytesIO(img_bytes))
        if detect_teeth_with_yolo(path_to_image):
            uploaded_img.is_recognized = True

        return Response('ok')