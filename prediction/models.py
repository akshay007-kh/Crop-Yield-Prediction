from django.db import models


class CropPrediction(models.Model):

    crop_name = models.CharField(max_length=100)

    area = models.FloatField()

    rainfall = models.FloatField()

    temperature = models.FloatField()

    humidity = models.FloatField()

    soil_ph = models.FloatField()

    fertilizer = models.FloatField()

    irrigation = models.CharField(max_length=20)

    predicted_yield = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop_name