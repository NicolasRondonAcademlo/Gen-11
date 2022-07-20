from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
router = DefaultRouter()
router.register("notas", NoteViewSet)

urlpatterns = router.urls