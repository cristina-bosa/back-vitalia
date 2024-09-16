from rest_framework import routers

from administration.views.request_access import RequestAccessViewSet
from administration.views.users import UserAdminViewSet

router = routers.DefaultRouter()
router.register('request-access', RequestAccessViewSet, basename = 'request')
router.register('users', UserAdminViewSet, basename = 'user')
router.urlpatterns = router.urls