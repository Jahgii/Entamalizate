from django.shortcuts import render


def home(request):
    print request
    num=12
    return render(request, 'home.html', {'Num': num})

def Pedido(request):
    print request
    num=12
    return render(request, 'Pedidos.html', {'Num': num})

# Create your views here.
