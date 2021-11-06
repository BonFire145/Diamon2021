from django.shortcuts import render
from .models import bloodinfo, bloodinfo_origin
from rest_framework import viewsets
from .serializers import *
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from rest_framework import status
from board import one_data_predict as OneDataPredict

# Create your views here.


class BloodinfoViewSet(viewsets.ModelViewSet):
    queryset = bloodinfo.objects.all()
    serializer_class = bloodinfoSerializer


class BloodinfoOriginViewSet(viewsets.ModelViewSet):
    queryset = bloodinfo_origin.objects.all()
    serializer_class = bloodinfoOriginSerializer


class BloodinfoListAPIView(GenericAPIView):
    serializer_class = bloodpredicSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        if serializer.is_valid():
            data = serializer.data
            res = OneDataPredict.Prediction([data[key] for key in data])
            predict_json = {"pred_val": res}
            data.update(predict_json)
            return JsonResponse({"pred_val": res}, status=status.HTTP_200_OK)
            # return JsonResponse(data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
