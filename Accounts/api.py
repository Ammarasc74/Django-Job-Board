from .models import Profile
from .serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User


class User_Api(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer


class All_Users_Api(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer


class User_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class =  userSerializer
    lookup_field = 'id'


# class User_login_Api(generics.LoginAPIView):
#     queryset = User.objects.all()
#     serializer_class =  userSerializer
#     lookup_field = 'id'

    
    