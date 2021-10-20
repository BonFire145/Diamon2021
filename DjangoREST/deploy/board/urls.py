from django.urls import path
from board.views import *
urlpatterns = [
    path("bloodinfo",BloodinfoListAPIView.as_view())
]

