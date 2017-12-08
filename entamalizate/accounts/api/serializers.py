
from django.contrib.auth import get_user_model
from rest_framework import serializers
from Tamales.models import  Productos

User =  get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class ProductosDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = [
            'Nombre',
            'Precio',
            'imagen'
        ]
