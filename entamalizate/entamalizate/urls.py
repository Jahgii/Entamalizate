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
from Tamales.views import ProductosVista, ClientesVista, Registro_orden, Hacer_Pedido
from Tamales.views import TamalesCreateView, RegistrationView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^pedido$', views.Pedido, name='pedido'),
    url(r'^tamales/consulta1$', ProductosVista.as_view(), name='consulta1'),
    url(r'^tamales/consulta2$', ClientesVista.as_view(), name='consulta2'),
    url(r'^tamales/consulta3$', Registro_orden, name='consulta3'),
    url(r'^tamales/ordenar$', Hacer_Pedido, name='consulta3'),
    url(r'^tamales/create$', TamalesCreateView.as_view(), name='tamales_create'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
