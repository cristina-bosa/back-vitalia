from rest_framework import routers

from doctors.views.doctor import DoctorViewSet

router = routers.DefaultRouter()
router.register('', DoctorViewSet, basename = 'doctor')
router.urlpatterns = router.urls
