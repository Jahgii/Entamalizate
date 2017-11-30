from django import forms

from .models import Pedido_Productos, Pedidos

class TamalesModelForm(forms.ModelForm):

    class Meta:
        model = Pedido_Productos
        fields = [
            "Pedido",
            "Producto",
            "Cantidad",
            "Total_Pagar"
            ]
