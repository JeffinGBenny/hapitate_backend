from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import permissions
from rest_framework import generics
# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny


class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    permission_classes = [AllowAny]


class VendorDetail(APIView):
    '''
    Crud functionality for Vendor
    '''

    def get_object(self, pk):
        try:
            return models.Vendor.objects.get(pk=pk)
        except models.Vendor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.VendorDetailSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.VendorDetailSerializer(
            snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailPageSerializer
    permission_classes = [AllowAny]


class CustomerDetail(APIView):

    def get_object(self, pk):
        try:
            return models.Customer.objects.get(pk=pk)
        except models.Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.CustomerDetailPageSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.CustomerDetailPageSerializer(
            snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomUserList(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserRegisterSerializer
    permission_classes = [AllowAny]


class CustomUserDetail(APIView):

    def get_object(self, pk):
        try:
            return models.CustomUser.objects.get(pk=pk)
        except models.CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.CustomUserRegisterSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.CustomUserRegisterSerializer(
            snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)