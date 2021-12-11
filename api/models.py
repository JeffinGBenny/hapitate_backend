from django.db import models
from django import forms
from django.forms import widgets

'''
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(max_length=10)
    def __str__(self):
        return self.first_name
'''

class Vendor(models.Model):
    VENDOR_STATUS = (
        ('Active', 'Active'),
        ('Disabled', 'Disabled'),
    )
    name = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    shopName = models.CharField(max_length=100, null=True, blank=True)
    mobileNumber = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=VENDOR_STATUS,
                              max_length=20, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    STATUS_CHOICE = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    name = models.CharField(max_length=40, default='', null=False, blank=False)
    slug = models.SlugField()
    icon = models.CharField(max_length=2000)
    allow_featured_category = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICE, default='Active', null=True, blank=True, max_length=10)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    STATUS_CHOICE = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    status = models.CharField(choices=STATUS_CHOICE, default='Active', null=True, blank=True, max_length=10)

    def __str__(self):
        return self.category.name+" - "+self.name        


class Product(models.Model):
    PRODUCT_STATUS_CHOICE = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    )
    # PRODUCT_TYPE_CHOICE = (
    #     ('Physical', 'Physical'),
    #     ('Digital', 'Digital'),
    #     ('Licensed', 'Licensed')
    # )
    PRODUCT_STOCK_CHOICE = (
        ('Unlimited', 'Unlimited'),
        ('Limited', 'Limited'),
    )
    PRODUCT_DISCOUNT_CHOICE = (
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
    )
    PRODUCT_CATEGORY_CHOICE = (
        ('Breakfast', 'Breakfast'),
        ('Snacks', 'Snacks'),
        ('Beverages', 'Beverages'),
        ('Grocery', 'Grocery'),
        ('Nutrition', 'Nutrition'),
        ('Organic Foods', 'Organic Foods'),
        ('Pet Lovers', 'Pet Lovers'),
    )
    PRODUCT_SUBCATEGORY_CHOICE = (
        ('Oats', 'Oats'),
        ('Flour', 'Flour'),
        ('Muesli', 'Muesli'),
        ('Exotic Coffe', 'Exotic Coffe'),
        ('Mens Nutrition', 'Mens Nutrition'),
        ('Womens Nutrition', 'Womens Nutrition'),
    )
    Name = models.CharField(max_length=30, null=True, blank=True)
    Type = models.CharField(default='Physical', max_length=20, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    subcategory = models.CharField(choices=PRODUCT_SUBCATEGORY_CHOICE, default=PRODUCT_SUBCATEGORY_CHOICE[0][0], max_length=50)
    category = models.CharField(choices=PRODUCT_CATEGORY_CHOICE, default=PRODUCT_CATEGORY_CHOICE[0][0], max_length=50)
    Status = models.CharField(choices=PRODUCT_STATUS_CHOICE , default='Available', max_length=20, null=True, blank=True)
    Stock = models.CharField(choices=PRODUCT_STOCK_CHOICE, default='Limited', max_length=20, null=True, blank=True)
    Options = models.CharField(max_length=20, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    discount = models.CharField(choices=PRODUCT_DISCOUNT_CHOICE, max_length=20 ,null=True, blank=True)
    def __str__(self):
        return self.Name


class Coupon(models.Model):
    COUPON_TYPE_CHOICES = (
        ('Discount By amount', 'Discount By Amount'),
        ('Discount By percentage', 'Discount By percentage'),
    )
    code = models.CharField(max_length=6, null=False, blank=False)
    Type = models.CharField(choices=COUPON_TYPE_CHOICES, max_length=30)
    quantity = models.IntegerField(default=100, null=False, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.code


class SubscriptionPlan(models.Model):
    SUBS_TYPE_CHOICES = (
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Unlimited', 'Unlimited')
    )
    SUBS_CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('INR', 'INR'),
    )
    SUBS_DURATION_CHOICES = (
        ('1-Year', '1-Year'),
        ('2-Year', '2-Year'),
        ('3-Year', '3-Year'),
    )
    SUBS_PRODUCT_ALLOWED_CHOICES = (
        ('Unlimited', 'Unlimited'),
        ('Limited', 'Limited'),
    )
    SUBS_PLAN_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Removed', 'Removed'),
    )
    Type = models.CharField(
        max_length=10, choices=SUBS_TYPE_CHOICES, null=True, blank=True)
    Currency = models.CharField(
        max_length=10, choices=SUBS_CURRENCY_CHOICES, null=True, blank=True)
    Cost = models.IntegerField(null=True, blank=True)
    Duration = models.CharField(max_length=10, choices=SUBS_DURATION_CHOICES)
    ProductsAllowed = models.CharField(
        max_length=10, choices=SUBS_PRODUCT_ALLOWED_CHOICES, blank=True, null=True)
    PlanStatus = models.CharField(
        max_length=10, null=True, blank=True, choices=SUBS_PLAN_STATUS_CHOICES)

    def __str__(self):
        return self.Type

class Currency(models.Model):
    CURRENCY_NAME_CHOICE = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('INR', 'INR')
    )
    name = models.CharField(choices=CURRENCY_NAME_CHOICE, null=True, blank=True, max_length=10)
    sign = models.CharField(max_length=10, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
