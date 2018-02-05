from django.contrib import admin

# Register your models here.

from .models import Topping, Pizza,Post,User,PostLike

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostLike)

