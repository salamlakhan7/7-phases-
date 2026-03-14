#from django.contrib.auth import authenticate, login, logout
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Test
#from .serializers import TestSerializer, RegisterSerializer, LoginSerializer
from .permissions import IsAdminGroup, IsOwnerOrReadOnly
from .serializers import TestSerializer , RegisterSerializer, LoginSerializer


# -------------------------------
# Test CRUD ViewSet
# -------------------------------

class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# -------------------------------
# Register API
# -------------------------------

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


# -------------------------------
# Login API : Based on Session Authentication or cookies
# -------------------------------

# class LoginView(APIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         username = serializer.validated_data["username"]
#         password = serializer.validated_data["password"]

#         user = authenticate(username=username, password=password)

#         if user is None:
#             return Response(
#                 {"error": "Invalid credentials"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         login(request, user)
#         return Response({"message": "Login successful"})


# -------------------------------
# Logout API : Based on Session Authentication or cookies
# -------------------------------

# class LogoutView(APIView):

#     def post(self, request):
#         logout(request)
#         return Response({"message": "Logout successful"})
    

#################### JWT Logout with Blacklisting ####################
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "JWT logout successful"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response(
                {"error": "Invalid token"},
                status=status.HTTP_400_BAD_REQUEST
            )

# views.py
#################### custom JWT token view to include extra claims ####################
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
   # permission_classes = [IsAuthenticated, IsAdminGroup]
    serializer_class = MyTokenObtainPairSerializer
    
############## custom token verfication about user group ##############
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminGroup

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminGroup]

    def post(self, request):
        return Response({"message": "POST allowed for Admin"})
    
import requests
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def google_login(request):
    print("REDIRECT URI:", settings.GOOGLE_REDIRECT_URI)

    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?response_type=code"
        f"&client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        "&scope=openid email profile"
        "&access_type=offline"
    )

    print("FULL AUTH URL:", google_auth_url)

    return redirect(google_auth_url)

##################### redirect url ######################

# def google_callback(request):
#     code = request.GET.get("code")

#     if not code:
#         return JsonResponse({"error": "No code provided"}, status=400)

#     # Exchange code for token
#     token_url = "https://oauth2.googleapis.com/token"

#     data = {
#         "code": code,
#         "client_id": settings.GOOGLE_CLIENT_ID,
#         "client_secret": settings.GOOGLE_CLIENT_SECRET,
#         "redirect_uri": settings.GOOGLE_REDIRECT_URI,
#         "grant_type": "authorization_code",
#     }

#     token_response = requests.post(token_url, data=data)
#     token_json = token_response.json()

#     access_token = token_json.get("access_token")

#     if not access_token:
#         return JsonResponse({"error": "Failed to get access token"}, status=400)

#     # Get user info
#     userinfo_url = "https://www.googleapis.com/oauth2/v2/userinfo"
#     userinfo_response = requests.get(
#         userinfo_url,
#         headers={"Authorization": f"Bearer {access_token}"}
#     )

#     userinfo = userinfo_response.json()

#     email = userinfo.get("email")
#     first_name = userinfo.get("given_name", "")
#     last_name = userinfo.get("family_name", "")

#     if not email:
#         response = requests.post("https://oauth2.googleapis.com/token", data=data)

#         print("STATUS:", response.status_code)
#         print("RESPONSE:", response.text)

#     # Create or get user
#     user, created = User.objects.get_or_create(
#         username=email,
#         defaults={
#             "email": email,
#             "first_name": first_name,
#             "last_name": last_name,
#         }
#     )

#     # Generate JWT
#     refresh = RefreshToken.for_user(user)

#     return JsonResponse({
#         "refresh": str(refresh),
#         "access": str(refresh.access_token),
#         "user": {
#             "email": user.email,
#             "first_name": user.first_name,
#         }
#     })
    
    ################## Save codes (jwt token) in httpOnly cookie ##################
    from django.http import JsonResponse

def google_callback(request):
    code = request.GET.get("code")

    if not code:
        return JsonResponse({"error": "No code provided"}, status=400)

    token_url = "https://oauth2.googleapis.com/token"

    data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(token_url, data=data)
    token_json = token_response.json()

    access_token = token_json.get("access_token")

    if not access_token:
        return JsonResponse({"error": "Failed to get access token"}, status=400)

    userinfo_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    userinfo_response = requests.get(
        userinfo_url,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    userinfo = userinfo_response.json()

    email = userinfo.get("email")
    first_name = userinfo.get("given_name", "")
    last_name = userinfo.get("family_name", "")

    if not email:
        return JsonResponse({"error": "Email not provided"}, status=400)

    user, created = User.objects.get_or_create(
        username=email,
        defaults={
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        }
    )

    refresh = RefreshToken.for_user(user)
    access = refresh.access_token

    response = JsonResponse({"message": "Login successful"})

    # 🔐 HttpOnly cookies
    response.set_cookie(
        key="access_token",
        value=str(access),
        httponly=True,
        secure=False,  # True in production (HTTPS)
        samesite="Lax"
    )

    response.set_cookie(
        key="refresh_token",
        value=str(refresh),
        httponly=True,
        secure=False,  # True in production
        samesite="Lax"
    )

    return response