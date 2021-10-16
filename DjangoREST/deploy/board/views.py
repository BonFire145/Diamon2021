from django.shortcuts import render
from .models import Posting, Comment, bloodinfo
from rest_framework import viewsets
from .serializers import PostingSerializer, CommentSerializer, bloodinfoSerializer

# Create your views here.


class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BloodinfoViewSet(viewsets.ModelViewSet):
    queryset = bloodinfo.objects.all()
    serializer_class = bloodinfoSerializer
