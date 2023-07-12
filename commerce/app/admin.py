from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(FeaturedIn)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)




class CommentsInline(admin.TabularInline):
     model = comments
     extra = 1

class CommentsAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]

admin.site.register(product, CommentsAdmin)
     




