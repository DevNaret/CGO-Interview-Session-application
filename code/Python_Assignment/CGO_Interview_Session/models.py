from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import int_list_validator
# from django_pg import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from models import Frog

# Create your models here.



class Frog(models.Model):
    X = models.IntegerField( verbose_name='X is last position on the falling leaves', validators=[MaxValueValidator(100000), MinValueValidator(1)])
    A = ArrayField(models.IntegerField( verbose_name='A are position where one leaf falls at time', validators=[MinValueValidator(1)]))




