from .models import *

def cart_count(request):
    if request.user.is_authenticated:
        cart= Cart.objects.filter(user=request.user)
        count=0
        for i in cart:
            count+=i.quantity
       
            
    else:
        count = 0
    return {'cart_count': count}


def categories(request):
    return {
        'allCategories': Category.objects.all()
    }


def wishlist_count(request):
    if request.user.is_authenticated:
        count = Wishlist.objects.filter(user=request.user).count()
    else:
        count = 0
    return {'wishlist_count': count}


