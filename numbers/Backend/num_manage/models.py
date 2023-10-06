from django.db import models

# Create your models here.

# numbers/models.py
from django.db import models

class MergedNumbers(models.Model):
    numbers = models.JSONField()
