from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlanetSerializer,UserSerialzer
from .models import Planet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
# Create your views here.

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all().order_by('id')
    serializer_class = PlanetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
    permission_classes = (AllowAny,)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('name')
#     serializer_class = UserSerialzer
#     permission_classes = [IsAuthenticatedOrReadOnly]
