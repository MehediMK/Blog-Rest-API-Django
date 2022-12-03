from rest_framework import generics
from api.serializers import Userserializers
from django.contrib.auth.models import User

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializers

class UserAPIDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializers