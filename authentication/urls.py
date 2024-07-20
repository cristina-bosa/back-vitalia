from rest_framework import routers

from authentication.views.auth import AuthViewSet

router = routers.DefaultRouter()
router.register('', AuthViewSet, basename = 'auth')

router.urlpatterns = router.urls

