from django.db import models


# Create your models here.
class User(models.Model):
    nanme = models.CharField(max_length=50)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Admin(User):
    proxy = True

    def drop(self, user):
        user.delete()


class Staff(User):
    class Meta:
        proxy = True

    def block(self,user):
        user.is_block =True
        user.save