from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, UserViewSet
router = DefaultRouter()
router.register("users",UserViewSet)
router.register("notes",NoteViewSet)

urlpatterns = router.urls