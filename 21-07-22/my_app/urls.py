from django.db import router
from rest_framework.routers import DefaultRouter
from .views import MyViewSet

router = DefaultRouter()
router.register("my_url", MyViewSet)

urls = router.urls