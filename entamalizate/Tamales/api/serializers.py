from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from .models import  Pedidos

class PedidoModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Pedidos
        fields = [
            'user',
            'content',
            'created',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.created.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.created) + " ago"
