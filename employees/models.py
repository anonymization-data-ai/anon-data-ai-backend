from django.db import models

class Employee(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    poste = models.CharField(max_length=100)
    niveau_seniorite = models.CharField(max_length=50)
    date_embauche = models.DateField()
    salaire_brut_annuel = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_annuel = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(
        max_length=50,
        choices=[("Actif", "Actif"), ("En congé", "En congé"), ("Partant", "Partant")]
    )

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.poste}"
