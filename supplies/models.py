from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Supply(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f'[{self.id}] {self.name} : {self.description}'