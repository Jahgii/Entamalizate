from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from Tamales.models import Pedidos
from .serializers import PedidoModelSerializer

class PedidoCreateAPIView(generics.CreateAPIView):
    serializer_class = PedidoModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PedidoListAPIView(generics.ListAPIView):
    serializer_class = PedidoModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Pedidos.objects.all().order_by("-Fecha_Final")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(ID_Pedido__icontains=query) |
                            Q(user__username__icontains=query)
                          )
        return qs
