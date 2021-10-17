from django.db import models
from django.db.models import fields
from .models import Posting, Comment, bloodinfo
from rest_framework import serializers


class PostingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posting
        fields = ('name', 'title', 'text')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('posting', 'name', 'text')


class bloodinfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bloodinfo
        fields = ('param1', 'param2', 'param3', 'param4', 'param5', 'param6', 'param7', 'param8', 'param9')
        #fields = '__all__'