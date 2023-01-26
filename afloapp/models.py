from django.db import models

# Create your models here.

class Formateur(models.Model):
    nom=models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nom}"

class Eleve(models.Model):
    nom=models.CharField(max_length=30)  

    def __str__(self) -> str:
        return f"{self.nom}"  

class Information(models.Model):
    information=models.TextField()

    def __str__(self) -> str:
        return f"{self.information}"

class Formation(models.Model):
    nom = models.CharField(max_length=30)
    description = models.TextField(default="Non communiquée...", null=True)
    diplomante = models.BooleanField(default=True)

    formateur = models.ForeignKey( #clefs étrangère pour lier les tables
        Formateur,
        related_name='formations', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL)

    eleves = models.ManyToManyField( #relation plusieurs à plusieurs
        Eleve, 
        related_name='formations', 
        null=True, 
        blank=True)

    information = models.OneToOneField(
        Information, 
        related_name='formation', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE)    


    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nom}"




