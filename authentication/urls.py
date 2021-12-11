from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('v1/users/', views.CustomUserList.as_view(), name='users'),
    path('v1/user/<int:pk>/', views.CustomUserDetail.as_view(), name='user'),
    path('v1/customers/', views.CustomerList.as_view(), name='customers'),
    path('v1/customer/<int:pk>/',
         views.CustomerDetail.as_view(), name='customer_detail'),
    path('v1/vendors/', views.VendorList.as_view(), name='vendors'),
    path('v1/vendor/<int:pk>', views.VendorDetail.as_view(), name='vendor'),
]