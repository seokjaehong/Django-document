from django.contrib import admin

# Register your models here.

from .models import (
    #basic
    Topping, Pizza,
    #intermediate
    Post,User,PostLike,
    #self
    FacebookUser,
    #symmetrical_intermediate
    TwitterUser,Relation,
    #symmetrical
    InstagramUser,


)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(FacebookUser)
admin.site.register(TwitterUser)
admin.site.register(Relation)
admin.site.register(InstagramUser)