from django.db import models

# Create your models here.
from django.db.models import CharField


class Shop(models.Model):
    name = CharField(max_length=100)
