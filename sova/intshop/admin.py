from django.contrib import admin
from .models import *
from domain.models import User

admin.site.register(Product_movie)
admin.site.register(Category_product)
admin.site.register(Product_book)
admin.site.register(Product_music)
admin.site.register(User)

