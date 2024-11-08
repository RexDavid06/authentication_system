from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Info
from .serializers import InfoSerializers

# Create your views here.
class InfoViews(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers


    def delete(self, *args, **kwargs):
        Info.objects.all().delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
