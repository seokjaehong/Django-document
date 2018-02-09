from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name} | {self.address}'


class Restaurant(Place):
    serve_hot_dogs = models.BooleanField(default=False)
    serve_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'Restaurant {sef.name} | {self.address}'
