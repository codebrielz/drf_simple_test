# Rest framework me proporciona ya la rutas basicas (CRUD) de estos datos
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects') #nombre de la ruta y despues indicamos que esta basado en el conjunto de datos que viene desde viewSet 
# y como tercer parametro indicamos el nombre de la ruta

urlpatterns = router.urls

