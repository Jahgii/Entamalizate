from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from Tamales.models import Pedidos, Pedido_Productos
from .pagination import StandardResultPagination
from .serializers import PedidoModelSerializer, PedidoProductosModelSerializer

class PedidoCreateAPIView(generics.CreateAPIView):
    serializer_class = PedidoModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PedidoListAPIView(generics.ListAPIView):
    serializer_class = PedidoModelSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self, *args, **kwargs):
        qs = Pedidos.objects.all().order_by("-ID_Pedido")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(ID_Pedido__icontains=query)|
                            Q(user__username__icontains=query)
                          )
        return qs

class PedidoProductosCreateAPIView(generics.CreateAPIView):
    serializer_class = PedidoProductosModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PedidoProductosListAPIView(generics.ListAPIView):
    serializer_class = PedidoProductosModelSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self, *args, **kwargs):
        qs = Pedido_Productos.objects.all().order_by("-ID")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(Cantidad__icontains=query)|
                            Q(ID__icontains=query)|
                            Q(Pedido__ID_Pedido__icontains=query)
                          )
        return qs
