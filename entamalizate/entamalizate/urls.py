"""entamalizate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from .views import home
from . import views
from accounts.views import UserRegisterView

    #Funciones
from Tamales.views import Registro_orden, Hacer_Pedido

    #Clases
from Tamales.views import PedidoDeleteView, Pedido_ProductosDeleteView, Pedido_ProductosCreateView
from Tamales.views import Pedido_ProductosUpdateView, PedidoCreateView, Pedido_ProductosListView, PedidosListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',      views.home, name='home'),
        #Funciones no se usaran ya que haremos todo con vistas
    # url(r'^pedido$',            views.Pedido, name='pedido'),
    # url(r'^tamales/ordenar$',   Hacer_Pedido, name='VistaOrdenes'),
        #Vistas
    url(r'^tamales/lista/detalle$',                      Pedido_ProductosListView.as_view(),   name='pedido_productos_lista'),
    url(r'^tamales/lista$',                              PedidosListView.as_view(),            name='pedidos_lista'),
    url(r'^tamales/orden/(?P<pk>\d+)/delete/$',          PedidoDeleteView.as_view(),           name='pedidos_delete'),
    url(r'^tamales/orden/create/$',                      PedidoCreateView.as_view(),           name='pedidos_create'),
    url(r'^tamales/orden/producto/(?P<pk>\d+)/delete/$', Pedido_ProductosDeleteView.as_view(), name='producto_delete'),
    url(r'^tamales/orden/producto/(?P<pk>\d+)/create/$', Pedido_ProductosCreateView.as_view(), name='producto_create'),
    url(r'^tamales/orden/producto/(?P<pk>\d+)/update/$', Pedido_ProductosUpdateView.as_view(), name='producto_update'),
        #path
    url(r'^static/(?P<path>.*)$',   serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$',    serve, {'document_root': settings.MEDIA_ROOT}),
        #api
    url(r'^api/tamales/', include ('Tamales.api.urls', namespace = 'tamales_api')),
        #accounts
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
