import datetime
from datetime import timezone

from django.db import models

# Create your models here.


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings =models.ManyToManyField(Topping)

    def __str__(self):
        return  self.name



#EXTRA FIELDS ON MANY-TO-MANY RELATIONSHIPS

class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        related_name='like_posts',
    )

    def __str__(self):
        return self.title

class User(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return  self.name

class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        # return f'{self.post.title}글의 좋아요({self.user.name},{self.created_date})'
        return '"{title}"글의 좋아요({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            date=datetime.strftime(
                timezone.make_navie((self.created_date),'%Y.%m,%d'),

        )