from django.contrib import admin
from .models import Product, SubscriptionPlan, Coupon, Vendor, SubCategory, Category, Currency
# Register your models here.


admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Coupon)
admin.site.register(SubscriptionPlan)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Currency)