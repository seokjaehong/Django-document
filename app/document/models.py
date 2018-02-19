from django.db import models

# Create your models here.
class Musicion(models.Model):
    first_name  =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    instrument = models.CharField(max_length = 100, blank=True)

class Album (models.Model):
    artist = models.ForeignKey(Musicion,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField(
        blank = True,
        null = True
    )
    #null True를 하면 마이그레이션을 새로해줘야함
    num_stars = models.IntegerField()

class Person(models.Model) :
    SHIRT_SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('l','Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZES)

    def __str__(self):
        return (f'{self.name} pk:{self.pk} 셔츠 사이즈: {self.shirt_size})')
        # return '{name} {pk} {shirt_size}.
