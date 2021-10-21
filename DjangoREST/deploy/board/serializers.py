from django.db import models
from django.db.models import fields
from .models import bloodinfo
from rest_framework import serializers

class bloodinfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bloodinfo
        fields = ('param1', 'param2', 'param3', 'param4', 'param5', 'param6', 'param7', 'param8')
class bloodpredicSerializer(serializers.ModelSerializer):
    class Meta:
        model = bloodinfo
        fields = ('param1', 'param2', 'param3', 'param4', 'param5', 'param6', 'param7', 'param8')