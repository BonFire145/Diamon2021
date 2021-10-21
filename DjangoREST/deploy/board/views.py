from django.shortcuts import render
from .models import Posting, Comment, bloodinfo
from rest_framework import viewsets
from .serializers import PostingSerializer, CommentSerializer, bloodinfoSerializer
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from rest_framework import status
from board import one_data_predict as OneDataPredict

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

class BloodinfoListAPIView(GenericAPIView):
    serializer_class = bloodinfoSerializer
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        if serializer.is_valid():
            data = serializer.data
            print([data[key] for key in data])
            res =  OneDataPredict.Prediction([data[key] for key in data])
            print(res)
            return JsonResponse({"pred_val": float(res)}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)