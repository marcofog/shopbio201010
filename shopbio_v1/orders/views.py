from django.shortcuts import render
from .models import Ordini_dettaglio
from store.models import CostoConsegna, OrarioConsegna
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)
    costo_consegna=CostoConsegna.objects.all()
    orario_consegna=OrarioConsegna.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            print(cart)
            for item in cart:
                Ordini_dettaglio.objects.create(id_ordine=order,nome_prodotto=item['product'],prezzo_quantità=item['price'],q_quantità=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,'orders/order/created.html',{'order': order})
    else:
        form = OrderCreateForm()
        return render(request,'orders/order/create.html',{'cart': cart, 'form': form, 'costo_consegna':costo_consegna, 'orario_consegna':orario_consegna})
