from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import PedidoListAPIView, PedidoCreateAPIView, PedidoProductosCreateAPIView, PedidoProductosListAPIView

urlpatterns=[
    url(r'^$', PedidoListAPIView.as_view(), name = 'list'),
    url(r'^create/$', PedidoCreateAPIView.as_view(), name='create'),
    url(r'^pp/$', PedidoProductosListAPIView.as_view(), name = 'list_pp'),
    url(r'^pp/create/$', PedidoProductosCreateAPIView.as_view(), name='create_pp'),

]
