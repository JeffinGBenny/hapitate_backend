from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    #path('', views.getRoutes, name='routes'),
    path('v1/info/', views.CountProperties.as_view(), name='count'),
    path('v1/products/', views.ProductList.as_view(), name='products'),
    path('v1/product/<int:pk>/', views.ProductDetail.as_view(), name='product'),
    path('v1/coupons/', views.CouponList.as_view(), name='coupons'),
    path('v1/coupon/<int:pk>', views.CouponDetail.as_view(), name='coupon'),
    path('v1/vendors/', views.VendorList.as_view(), name='vendors'),
    path('v1/vendor/<int:pk>', views.VendorDetail.as_view(), name='vendor'),
    path('v1/vendor/register/',views.vendorRegister,name='vendorRegister'),
    path('v1/subsciptionplans/', views.SubscriptionPlanList.as_view(),name='subsciptionplans'),
    path('v1/subsciptionplan/<int:pk>',views.SubsciptionPlanDetail.as_view(), name='subsciptionplan'),
    # currencies
    path('v1/currencies/', views.CurrencyList.as_view(),name='currency'),
    # Category
    path('v1/categories/', views.CategoryList.as_view(),name='categories'),
    path('v1/category/<int:pk>',views.CategoryDetail.as_view(), name='category'),
    # SubCategory
    path('v1/subcategories/', views.SubCategoryList.as_view(),name='subcategories'),
    path('v1/subcategory/<int:pk>',views.SubCategoryDetail.as_view(), name='subsciptionplan'),
]
