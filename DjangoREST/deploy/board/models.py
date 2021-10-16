from django.db import models

# Create your models here.


class Posting(models.Model):
    title = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=30, blank=False)
    text = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    text = models.CharField(max_length=200, blank=False)


class bloodinfo(models.Model):
    param1 = models.FloatField(max_length=20, blank=False)
    param2 = models.FloatField(max_length=20, blank=False)
    param3 = models.FloatField(max_length=20, blank=False)
    param4 = models.FloatField(max_length=20, blank=False)
    param5 = models.FloatField(max_length=20, blank=False)
    param6 = models.FloatField(max_length=20, blank=False)
    param7 = models.FloatField(max_length=20, blank=False)
    param8 = models.FloatField(max_length=20, blank=False)
    param9 = models.IntegerField(max_length=20, blank=False)

    def __str__(self):
        return self.param1
