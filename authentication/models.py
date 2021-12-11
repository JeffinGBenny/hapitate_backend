from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.forms import IntegerField
from django.conf import settings

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class CustomUser(AbstractUser):
    CHOICES = (
        ('Customer', 'Customer'),
        ('Vendor', 'Vendor'),
    )
    role = models.CharField(
        max_length=20, choices=CHOICES, default=CHOICES[0][0])

    @property
    def customer(self):
        try:
            return Customer.objects.get(user=self)
        except Customer.DoesNotExist:
            default_value_of_buyer = {}
            # Or define default value at model fields
            return Customer.objects.create(user=self, **default_value_of_buyer)

    @property
    def vendor(self):
        try:
            return Vendor.objects.get(user=self)
        except Vendor.DoesNotExist:
            default_value_of_seller = {}
            # Or define default value at model fields
        return Vendor.objects.create(user=self, **default_value_of_seller)


class Customer(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,
                                on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.IntegerField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    dob = models.DateField()

    def __str__(self):
        return "Customer - " + self.user.username


class Vendor(models.Model):
    VENDOR_STATUS = (
        ('Active', 'Active'),
        ('Disabled', 'Disabled'),
    )
    COUNTRY_CHOICE = (
        ('India', 'India'),
    )
    STATE_CHOICES = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
                     ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True, on_delete=models.CASCADE, related_name='vendor_profile')
    store_name = models.CharField(max_length=300, unique=True)
    # address_1 = models.URLField(unique=True)
    address_2 = models.TextField(max_length=200, null=True, blank=True)
    address_2 = models.TextField(max_length=200, null=True, blank=True)
    country = models.CharField(choices=COUNTRY_CHOICE, max_length=200)
    city = models.CharField(max_length=50)
    state_county = models.CharField(
        choices=STATE_CHOICES, max_length=255, null=True, blank=True)
    zipcode = models.SmallIntegerField()
    store_phone = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True)
    company_inc = models.FileField(upload_to='files')
    company_pan_card = models.IntegerField(unique=True)
    fssai_license = models.FileField(upload_to='files', max_length=100)
    gst_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=VENDOR_STATUS,
                              max_length=20, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "Vendor- "+self.user.username