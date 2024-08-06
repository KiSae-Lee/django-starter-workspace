from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .serializer import UserSerializer


class UserAPI(viewsets.ViewSet):
    queryset = User.objects.all()

    def retrieve(self, request, pk=None):
        return Response("Retrieve method is not ready, yet", status=501)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=201)
            return Response("User created successfully", status=201)
        # return Response(serializer.errors, status=400)
        return Response("Request data is not valid", status=401)

    def update(self, request, pk=None):
        return Response("Update method is not ready, yet", status=501)

    def destroy(self, request, pk=None):
        return Response("Destroy method is not ready, yet", status=501)

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)
