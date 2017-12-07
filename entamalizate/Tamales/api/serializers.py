from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from Tamales.models import  Pedidos

class PedidoModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Pedidos
        fields = [
            'user',
            'ID_Pedido',
            'Cliente',
            'Fecha_Inicio',
            'Fecha_Final',
            'Metodo_Pago',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.Fecha_Inicio.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.Fecha_Inicio) + " ago"
