# serializers.py in the users Django app
from re import L
from django.forms import fields
from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Customer, CustomUser, Vendor


class CustomUserRegisterSerializer(RegisterSerializer):
    CHOICES = (
        ('Customer', 'Customer'),
        ('Vendor', 'Vendor'),
    )
    role = serializers.ChoiceField(choices=CHOICES)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['role'] = self.validated_data.get('role', '')
        return data_dict


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = (
        #     'username',
        #     'email',
        #     'password'
        # )


class CustomerDetailPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"