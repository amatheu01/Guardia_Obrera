from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'planificacion', Planificacion_ViewSet)
router.register(r'region_guardia', RegionGuardia_ViewSet)
router.register(r'posta', Posta_ViewSet)
router.register(r'grupo_guardia', GrupoGuardia_ViewSet)
router.register(r'tipo_incidencia', TipoIncidencia_ViewSet)
router.register(r'variable', Variable_ViewSet)
router.register(r'horario', Horario_ViewSet)
router.register(r'turno', Turnos_ViewSet)
router.register(r'patron', Patrones_ViewSet)

urlpatterns = router.urls
