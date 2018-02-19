from django.db import models

__all__ =(
    'Place',
    'Restaurant',
    'Waiter',
)
# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=50)
    address =models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name} the place'

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.place.name}'

class Waiter(models.Model):
    restaurant =models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.restaurant}'