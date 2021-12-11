
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes

from  authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from .models import Currency, SubscriptionPlan, Vendor, Product, Coupon, Category, SubCategory
from .serializers import CurrencySerializer, ProductSerializer, SubscriptionPlanSerializer, VendorSerializer, UserSerializer, CouponSerializer, CategorySerializer, SubCategorySerializer
from rest_framework.permissions import IsAdminUser, AllowAny

# Create your views here.

'''
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serailizer = UserSerializer(users, many=True)
    return Response(serailizer.data)
# @csrf_exempt
@api_view(['POST'])
def handleLogin(request):
    if request.method == 'POST':
        print("Logging in User: ", request.data)
        loginUsername = request.data.get('username')
        loginPassword = request.data.get('password')
        print(loginUsername, loginPassword)
        user = authenticate(username=loginUsername, password=loginPassword)
        print("User Object: ", user)
        if user is not None:
            login(request, user)
            print("User Status: ", user.is_authenticated,
                  request.user.is_authenticated)
            if user.is_authenticated:
                data = {
                    'authenticated': user.is_authenticated,
                    'user': loginUsername
                }
                print("Status: ", data)
                # return Response(data)
            else:
                data = {
                    'authenticated': user.is_authenticated,
                    'user': loginUsername
                }
                print("Status: ", data)
        else:
            data = {
                'authenticated': False,
                'user': loginUsername
            }
        return Response(data)
    else:
        data = {
            'error': 'error'
        }
        return Response(data)
@csrf_exempt
@api_view(["POST"])
def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        print("Logging out user")
    return redirect('http://localhost:3000/page/account/login-auth')
@csrf_exempt
@api_view(["POST"])
def handleSignup(request):
    if request.method == 'POST':
        print("Register User: ", request.data)
        username = request.data.get('name')
        email = request.data.get('email')
        pass1 = request.data.get('pass1')
        pass2 = request.data.get('pass2')
        firstName = request.data.get('firstname')
        lastName = request.data.get('lastname')
        # CREATE USER
        if len(username) > 10:
            return redirect('http://localhost:3000/page/account/register?error=nameExcedded')
        if not username.isalnum():
            return redirect('http://localhost:3000/page/account/register?error=notAlphanum')
        if pass1 != pass2:
            return redirect('http://localhost:3000/page/account/register?error=passnotmatch')
        user = User.objects.create_user(username, email, pass1)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        # refresh = RefreshToken.for_user(user)
        print(username, pass1)
        messages.success(request, "Account succesfully created")
        data = {
            'status': 'registered',
            'user': firstName
        }
        return JsonResponse(data)
        # return HttpResponse({
        #     "status": "Success",
        #     "user_id": user.id,
        #     "refresh": str(refresh),
        #     "access": str(refresh.access_token)
        # })
    else:
        data = {
            'status': "error"
        }
        return JsonResponse(data)
'''



class ProductList(APIView):
    # Product List view with the funcionality of of getting a list and posting to the list of products.

    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("ProdutDetail",request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    # Crud functionality for Products

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [AllowAny]

# CATEGORY DETAILS
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryDetail(APIView):
    '''
    Crud functionality for SubsciptionPlan
    '''

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SUB CATEGORY DETAILS
class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [AllowAny]


class SubCategoryDetail(APIView):
    '''
    Crud functionality for SubsciptionPlan
    '''

    def get_object(self, pk):
        try:
            return SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SubCategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SubCategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [AllowAny]


class VendorDetail(APIView):
    # Crud functionality for Vendor

    def get_object(self, pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VendorSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VendorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def vendorRegister(request):
    if request.method=='POST':
        name=request.data.get('name')
        password=request.data.get('password')
        address=request.data.get('address')
        shopName=request.data.get('shopName')
        mobileNumber=request.data.get('mobileNumber')
        email=request.data.get('email')
        description=request.data.get('description')
        vendor=Vendor.objects.create(name=name,address=address,shopName=shopName,mobileNumber=mobileNumber,email=email,description=description)
        vendor.save()
        # serializer=VendorSerializer(vendor)
        # return Response(serializer.data,status=200)
        vendor=CustomUser.objects.create(username=name,password=password,email=email,role="Vendor")
        vendor.save()
        serializer=CustomUserSerializer(vendor)
        return Response(serializer.data,status=201)
        


'''
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''



class CouponList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [AllowAny]


class CouponDetail(APIView):
    '''
    Crud functionality for Coupon
    '''

    def get_object(self, pk):
        try:
            return Coupon.objects.get(pk=pk)
        except Coupon.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CouponSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CouponSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionPlanList(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [AllowAny]

@permission_classes([AllowAny])
class SubsciptionPlanDetail(APIView):
    '''
    Crud functionality for SubsciptionPlan
    '''

    def get_object(self, pk):
        try:
            return SubscriptionPlan.objects.get(pk=pk)
        except SubscriptionPlan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SubscriptionPlanSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SubscriptionPlanSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CountProperties(APIView):
    '''
        Return the count of total number of products,vendors and customers
    '''

    def get(self, request, format=None):
        vendor_count = Vendor.objects.all().count()
        product_count = Product.objects.all().count()
        #customer_count = Customer.objects.all().count()
        response = {
            "vendor_count": vendor_count,
            "product_count": product_count,
            # "customer_count": customer_count,
        }
        return Response(response, status=status.HTTP_200_OK)
        