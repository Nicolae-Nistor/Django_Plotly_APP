from django.db import models

# Create your models here.
class INDICATOR(models.Model):
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    value = models.FloatField()

    class Meta:
         ordering = ('year',)

