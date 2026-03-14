from rest_framework.routers import DefaultRouter
from .views import SecurePostViewSet

router = DefaultRouter()
router.register(r'secure-posts', SecurePostViewSet)

urlpatterns = router.urls