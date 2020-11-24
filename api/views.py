from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

@api_view(['POST'])
def UserRegisterView(request):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # User.objects.create_user(serializer.save())
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
