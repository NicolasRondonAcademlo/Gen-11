from rest_framework.routers import DefaultRouter
from core.views import CustomUserViewSet

router = DefaultRouter()
router.register("users", CustomUserViewSet)
urlpatterns = router.urls