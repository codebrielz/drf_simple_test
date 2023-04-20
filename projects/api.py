from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

# el viewset sirve para definir quien puede consultar el API
class ProjectViewSet(viewsets.ModelViewSet):
    # Aqui indicamos que consultas se van a poder hacer
    queryset = Project.objects.all() #Conjunto de datos
    # permissions.AllowAny <-- significa que cualquier navegador cliente va a poder solicitar datos a mi servidor
    permissions_classes = [permissions.AllowAny]
    # le indicamos que serializer va a estar utilizando estos datos, como lo va a convertir
    serializer_class = ProjectSerializer
