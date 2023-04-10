from rest_framework import serializers
from .models import Image

class DentalDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name', 'accuracy')