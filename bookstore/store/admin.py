from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
