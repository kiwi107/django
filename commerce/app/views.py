from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import *







   


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        address = request.POST["address"]
        phone = request.POST["phone"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username,email=email,password=password,address=address,phone_number=phone)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")
    



def category(request, name):
    selectedCategory = Category.objects.get(name=name)
    allProducts = product.objects.filter(category=selectedCategory)
    inwishlist=[]
    for item in allProducts:
        try:
            wishlist = Wishlist.objects.get(user=request.user, product=item)
            inwishlist.append(True)
        except Wishlist.DoesNotExist:
            inwishlist.append(False)

    wishlist_product = zip(allProducts, inwishlist)

    
    return render(request, "app/category.html", {
        "allProducts": wishlist_product,
        "selectedCategory": selectedCategory,
    })


def productDetail(request, id):
    Product = product.objects.get(pk=id)
    allComments = comments.objects.filter(product=Product)
    allComments = list(allComments)
    allComments.reverse()
    allColors=Product.color.all()
    allSizes=Product.size.all()

    return render(request, "app/productDetail.html", {
        "Product": Product,
        "allComments": allComments,
        "allColors":allColors,
        "allSizes":allSizes,

    
       
    })


def comment(request, id):
    if request.method == "POST":
        currentUser = request.user
        Product = product.objects.get(pk=id)
        comment = request.POST["comment"]
        if comment=="":
            return JsonResponse({"message": "empty"})
        else:
            newComment = comments(product=Product, user=currentUser, comment=comment)
            newComment.save()
            return JsonResponse({
                "comment": newComment.comment,
                "user": newComment.user.username,
                "message": "added",
            })
    


def Cart_view(request):
    cart = Cart.objects.filter(user=request.user)
    total=0
    for item in cart:
        total=item.product.price*item.quantity + total
      

    return render(request,"app/cart.html",{
        "cart": cart,
        "total":total, 
    })

def index(request):
   featuredIn=FeaturedIn.objects.all()

   return render(request, "app/index.html",{
         "featuredIn":featuredIn,
         
   })

    




def addToCart(request):
    if request.method == "POST":
        currentUser = request.user
        productIdFromForm = request.POST["id"]
        colorFromForm = request.POST["color"]
        sizeFromForm = request.POST["size"]
        quantityFromForm = request.POST["quantity"]
       
        try:
            colorChosen = Color.objects.get(name=colorFromForm)
            sizeChosen = Size.objects.get(name=sizeFromForm)
            Product = product.objects.get(pk=productIdFromForm)
            cart = Cart(user=currentUser, product=Product, color=colorChosen, size=sizeChosen, quantity=quantityFromForm)
            cart.save()
            return JsonResponse({"message": "added",
                                 "quantity": quantityFromForm,})
        
        except Size.DoesNotExist:
            return JsonResponse({"messageSize": "no size"})
        
        except Color.DoesNotExist:
            return JsonResponse({"messageColor": "no color"})
       
            



    


        
    

def removeFromCart(request,callingPage):
    if request.method == "POST":
        currentUser = request.user
        id = request.POST["id"]
        cartItem = Cart.objects.get(pk=id)
        cartItem.delete()
        total=0
        cart = Cart.objects.filter(user=currentUser)
        for item in cart:
            total=item.product.price*item.quantity + total
        return JsonResponse({"total": total,
                             "quantity": cartItem.quantity,}) 
        


def Wishlist_view(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, "app/wishlist.html", {
        "wishlist": wishlist,
    })

def addToWishlist(request,callingPage):
    if request.method == "POST":
        currentUser = request.user
        productIdFromForm = request.POST["id"]
        Product = product.objects.get(pk=productIdFromForm)
        try:
            wishlist = Wishlist.objects.get(user=currentUser, product=Product)
            wishlist.delete()
            action = "removed"
        except Wishlist.DoesNotExist:
            wishlist = Wishlist(user=currentUser, product=Product)
            wishlist.save()
            action = "added"

        return JsonResponse({"action": action})




    


# def removeFromWishlist(request,callingPage):
#     if request.method == "POST":
#         product_id = request.POST.get("id")
#         p=product.objects.get(pk=product_id)
     
#         wishlist_item = get_object_or_404(Wishlist, product_id=p.id, user=request.user)
#         wishlist_item.delete()
#         if callingPage=="wishlist":
#             return HttpResponseRedirect(reverse("wishlist"))
#         elif callingPage=="index":
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return HttpResponseRedirect(reverse("category", args=(wishlist_item.product.category,)))



# def placeOrder(request):
#     if request.method == "POST":
#         currentUser = request.user
#         cart = Cart.objects.filter(user=currentUser)
#         total=0
#         for item in cart:
#             total=item.product.price*item.quantity + total
#         order=Order(user=currentUser,total=total)
#         order.save()
#         for item in cart:
#             order.items.add(item)
#         cart.delete()
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return HttpResponseRedirect(reverse("index"))
        


def placeOrder(request):
    if request.method == "POST":
        #check if cart is empty
        currentUser = request.user
        cart = Cart.objects.filter(user=currentUser)
        if not cart:
            comment="Your cart is empty."
            return render(request, "app/cart.html", {
                "comment": comment
            })
        else:
            total = request.POST.get("total")
            current_user = request.user
            cart_items = Cart.objects.filter(user=current_user)
            order = Order(user=current_user, total=total)
            order.save()
            for item in cart_items:
                order_items = OrderItem(order=order, product=item.product, color=item.color, size=item.size, quantity=item.quantity)
                order_items.save()
                item.delete()
            return HttpResponseRedirect(reverse("trackOrder"))
            
    



def trackOrder(request):
    current_user = request.user
    orders = Order.objects.filter(user=current_user)
    orderItemsResult = []
    for order in orders:
        orderItems = OrderItem.objects.filter(order=order)
        orderItemsResult.append((order,orderItems))

    orderItemsResult.reverse()
    
    return render(request, "app/trackOrder.html", {"orderItemsResult": orderItemsResult})


def orderDetails(request, id):
    order = Order.objects.get(pk=id)
    orderItems = OrderItem.objects.filter(order=order)
    orderCount = 0
    for item in orderItems:
        orderCount=orderCount+item.quantity
 
    return render(request, "app/orderDetails.html", {"order": order, "orderItems": orderItems, "orderCount": orderCount})

        
        
def aboutUs(request):
    return render(request, "app/aboutUS.html")
        




      
