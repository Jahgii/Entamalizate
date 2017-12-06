from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import PedidoListAPIView, PedidoCreateAPIView

urlpatterns=[
    url(r'^$', PedidoListAPIView.as_view(), name = 'list'),
    url(r'^create/$', PedidoCreateAPIView.as_view(), name='create'),

]
