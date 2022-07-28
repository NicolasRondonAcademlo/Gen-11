from rest_framework.routers import DefaultRouter
from .views import NoteVieSet

router = DefaultRouter()
router.register("notes", NoteVieSet)
urlpatterns = router.urls