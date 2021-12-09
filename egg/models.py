from django.db import models


# Create your models here.
class Egg(models.Model):
    total = models.IntegerField()
    good = models.IntegerField()
    not_good = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
