from .models import Cart
 
def cart_total(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        return {'cart': cart}
    return {'cart': None} 