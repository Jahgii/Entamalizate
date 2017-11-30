# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Productos, Clientes, Pedido_Productos, Usuarios, Pedidos, Metodo_Pago
from django.views.generic import ListView, CreateView
from .forms import TamalesModelForm
#from .mixin import FormUserNeededMixin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, get_user_model, login

from registration import signals
from registration.views import RegistrationView as BaseRegistrationView


User = get_user_model()
# Create your views here.

class RegistrationView(BaseRegistrationView):
    """
    Registration via the simplest possible process: a user supplies a
    username, email address and password (the bare minimum for a
    useful account), and is immediately signed up and logged in.
    """
    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/'

class TamalesCreateView(CreateView):
    form_class = TamalesModelForm
    template_name = "Tamales/PedirPedido.html"
    success_url = "/tamales/consulta3"

class ProductosVista(ListView):
    template_name = "Tamales/VistaProductos.html"
    queryset = Productos.objects.all()

class ClientesVista(ListView):
    template_name = "Tamales/VistaClientes.html"
    queryset = Clientes.objects.all()

def Registro_orden(request):
    result_set01 = Pedidos.objects.all() #Cliente__ID_Cliente=2 ; filter(Pedido__Cliente=3)
    result_set02 = Pedido_Productos.objects.all()
    context = {
    "Pedidos": result_set01, "Productos_P": result_set02
    }
    return render(request, "Tamales/Ordenes.html", context)

def Hacer_Pedido(request):
    result_set01 = Pedidos.objects.all() #Cliente__ID_Cliente=2 ; filter(Pedido__Cliente=3)
    result_set02 = Pedido_Productos.objects.all()
    context = {
    "Pedidos": result_set01, "Productos_P": result_set02
    }
    return render(request, "Pedidos.html", context)
