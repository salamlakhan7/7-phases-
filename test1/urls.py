from rest_framework.routers import DefaultRouter
from .views import AdminOnlyView, MyTokenObtainPairView, TestViewSet
from .views import RegisterView,LogoutView #  LoginView,
from django.urls import path
from .views import google_login, google_callback

router = DefaultRouter()
router.register(r'tests',TestViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('logout/', LogoutView.as_view()),
    
    path("api/logout/", LogoutView.as_view(), name="jwt_logout"),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin-test/', AdminOnlyView.as_view()),
    
    path("auth/google/login/", google_login),
    path("auth/google/callback/", google_callback),
]
urlpatterns += router.urls
