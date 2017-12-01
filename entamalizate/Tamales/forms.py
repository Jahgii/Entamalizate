from django import forms

from .models import Pedido_Productos, Pedidos

class PedidosProductosModelForm(forms.ModelForm):

    class Meta:
        model = Pedido_Productos
        fields = [
            #"Pedido",
            "Producto",
            "Cantidad",
            "Total_Pagar"
            ]

class PedidosModelForm(forms.ModelForm):
    Fecha_Inicio = forms.DateField(widget= forms.SelectDateWidget(empty_label="Nothing"))
    Fecha_Final = forms.DateField(widget= forms.SelectDateWidget(empty_label="Nothing"))

    class Meta:
        model = Pedidos
        fields = [
            #"ID_Pedido",
            "Cliente",
            "Fecha_Inicio",
            "Fecha_Final",
            "Metodo_Pago"
            ]
