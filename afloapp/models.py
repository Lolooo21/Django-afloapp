from django.db import models

# Create your models here.

class Formation(models.Model):
    nom = models.CharField(max_length=30)
    description = models.TextField(default="Non communiquée...", null=True)
    diplomante = models.BooleanField(default=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)