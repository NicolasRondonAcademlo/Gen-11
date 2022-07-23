from rest_framework.routers import DefaultRouter
from core.views import CustomUserViewSet
from my_app.urls import urls as my_app_urls

router = DefaultRouter()
router.register("users", CustomUserViewSet)
urlpatterns = router.urls + my_app_urls