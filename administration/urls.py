from rest_framework import routers

from administration.views.doctor import DoctorAdminViewSet
from administration.views.users import UserAdminViewSet

router = routers.DefaultRouter()
router.register('doctor', DoctorAdminViewSet , basename = 'doctor')
router.register('user', UserAdminViewSet, basename = 'user')
router.urlpatterns = router.urls