from rest_framework.routers import DefaultRouter

from .views import Persona_ViewSet

router = DefaultRouter()
router.register(r'persona', Persona_ViewSet)

urlpatterns = router.urls
