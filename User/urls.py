from rest_framework.routers import DefaultRouter

from .views import InfoViewSet


router = DefaultRouter()
router.register('', InfoViewSet, basename= 'InfoViewset')
urlpatterns = router.urls