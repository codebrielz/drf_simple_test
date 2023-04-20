# Nos permite poder llamar un modulo especial de rest framework
from rest_framework import serializers
from .models import Project

# Esto nos va a permitir convertir un modelo en datos que van a poder ser consultados
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at') #Estos son los campos que ya tienen las tablas que se han creado a traves de Models.py
        read_only_fields = ('created_at', ) #Aquí van los campos de solo lectura (las tuplas deben terminar en ,)