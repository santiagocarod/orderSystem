from django.db import models
from django.core.validators import MinValueValidator
from supplies.models import *
# Create your models here.


class usesSupply(models.Model):
    supply = models.ForeignKey(Supply,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.supply} < {self.quantity} >'

class Product(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    supplies = models.ForeignKey(usesSupply,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'[{self.id}] {self.name}'