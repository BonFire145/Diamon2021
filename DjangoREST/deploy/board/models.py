from django.db import models

# Create your models here.


class bloodinfo(models.Model):
    param1 = models.FloatField(max_length=20, blank=False)
    param2 = models.FloatField(max_length=20, blank=False)
    param3 = models.FloatField(max_length=20, blank=False)
    param4 = models.FloatField(max_length=20, blank=False)
    param5 = models.FloatField(max_length=20, blank=False)
    param6 = models.FloatField(max_length=20, blank=False)
    param7 = models.FloatField(max_length=20, blank=False)
    param8 = models.FloatField(max_length=20, blank=False)
    param9 = models.IntegerField(blank=False)

    def __str__(self):
        return self.param1


class bloodinfo_origin(models.Model):
    param1 = models.IntegerField(blank=False)
    param2 = models.IntegerField(blank=False)
    param3 = models.IntegerField(blank=False)
    param4 = models.IntegerField(blank=False)
    param5 = models.IntegerField(blank=False)
    param6 = models.FloatField(max_length=20, blank=False)
    param7 = models.FloatField(max_length=20, blank=False)
    param8 = models.IntegerField(blank=False)
    param9 = models.IntegerField(blank=False)

    def __str__(self):
        return self.param1
