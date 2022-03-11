# myapi/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'device',views.DeviceViewSet)
router.register(r'medhistory',views.MedHistoryViewSet)
router.register(r'allergies', views.AllergiesViewSet)
router.register(r'medications',views.MedicationsViewset)
router.register(r'operation',views.OperationViewSet)
router.register(r'measurements',views.MeasurementsViewSet)
router.register(r'measurement',views.MeasurementViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]