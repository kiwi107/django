from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('category/<str:name>/', views.category, name='category'),
    path('product/<int:id>/', views.productDetail, name='product'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('removeFromCart/str:<callingPage>/', views.removeFromCart, name='removeFromCart'),
    path('cart', views.Cart_view, name='cart'),
    path('wishlist', views.Wishlist_view, name='wishlist'),
    path('addToWishlist/str:<callingPage>', views.addToWishlist, name='addToWishlist'),
    path('trackOrder', views.trackOrder, name='trackOrder'),
    path('placeOrder', views.placeOrder, name='placeOrder'),
    path('orderDetails/<int:id>/', views.orderDetails, name='orderDetails'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
