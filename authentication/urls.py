from rest_framework import routers

from authentication.views.auth import AuthViewSet
from authentication.views.choices import ChoicesViewSet
from doctors.views.city import CityViewSet
from doctors.views.specialty import SpecialtyViewSet

router = routers.DefaultRouter()
router.register('', AuthViewSet, basename = 'auth')
router.register('choices', ChoicesViewSet, basename = 'choices')
router.register('city', CityViewSet, basename= 'cities') #TODO: Cambiar de sitio
router.register('specialty', SpecialtyViewSet, basename = 'specialties')  #TODO: Cambiar de sitio
router.urlpatterns = router.urls
