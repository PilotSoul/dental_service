from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=('uploaded_teeth/'), blank=True)
    accuracy = models.FloatField(null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_recognized = models.BooleanField(default=False)
    recognized_path = models.CharField(max_length=255, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
