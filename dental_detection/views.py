from django.forms import model_to_dict
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from rest_framework import generics
import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from .image_recognition import *

from .models import Image


class DentalDetectionAPIView(APIView):
    def post(self, request):
        new_uuid = str(uuid.uuid4())[:7]
        uploaded_img = Image.objects.create(
            name=str(request.data['photo'])+new_uuid,
            photo=request.data['photo']
        )
        path_to_image = str(uploaded_img.photo)
        if recognized_image := detect_teeth_with_yolo(path_to_image, model_path="model_without_numbers"):
            uploaded_img.is_recognized = True
            uploaded_img.recognized_path = recognized_image
            img = open(uploaded_img.recognized_path, 'rb')
            return FileResponse(img)

        return Response('Teeth are not recognized')


class DentalDetectionNumbersAPIView(APIView):
    def post(self, request):
        new_uuid = str(uuid.uuid4())[:7]
        uploaded_img = Image.objects.create(
            name=str(request.data['photo'])+new_uuid,
            photo=request.data['photo']
        )
        path_to_image = str(uploaded_img.photo)
        if recognized_image := detect_teeth_with_yolo(path_to_image, model_path="model_with_numbers"):
            uploaded_img.is_recognized = True
            uploaded_img.recognized_path = recognized_image
            img = open(uploaded_img.recognized_path, 'rb')
            return FileResponse(img)

        return Response('Teeth are not recognized')