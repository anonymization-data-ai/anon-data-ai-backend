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
        choices=[("Actif", "Actif"), ("Conge", "Conge")]
    )
    
    date_naissance = models.DateField(null=True, blank=True)
    tranche_age = models.CharField(
        max_length=10,
        choices=[
            ("20-30", "20-30"),
            ("30-40", "30-40"),
            ("40-50", "40-50"),
            ("50-62", "50-62")
        ],
        null=True, blank=True
    )
    type_contrat = models.CharField(
        max_length=20,
        choices=[
            ("CIVP", "CIVP"),
            ("CDD", "CDD"),
            ("CDI", "CDI"),
            ("Alternance", "Alternance"),
            ("Stage", "Stage")
        ],
        null=True, blank=True
    )
    etat_civil = models.CharField(
        max_length=15,
        choices=[
            ("Célibataire", "Célibataire"),
            ("Marié(e)", "Marié(e)"),
            ("Divorcé(e)", "Divorcé(e)"),
            ("Veuf/Veuve", "Veuf/Veuve")
        ],
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.poste}"
