from django.urls import path, include
from board.views import *

urlpatterns = [
    path("bloodpredict",BloodinfoListAPIView.as_view())
]