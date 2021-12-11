from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from .models import Product, Vendor, Coupon, SubscriptionPlan, Category, SubCategory, Currency
from django.contrib.auth.models import User
from rest_framework import serializers




class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


'''
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
'''


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class SubscriptionPlanSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class SubCategorySerializer(ModelSerializer):
    category_name = serializers.CharField(
        source='category.name')

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'slug', 'category_name')      