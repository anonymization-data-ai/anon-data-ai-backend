import csv
from django.core.management.base import BaseCommand
from employees.models import Employee
from datetime import datetime

class Command(BaseCommand):
    help = "Import employees from CSV file"

    def handle(self, *args, **kwargs):
        file_path = "employes_IT.csv"  # Chemin du fichier CSV
        
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            employees_created = 0

            for row in reader:
                # Convertir les dates
                try:
                    date_embauche = datetime.strptime(row["date_embauche"], "%Y-%m-%d").date()
                except ValueError:
                    date_embauche = None

                try:
                    date_naissance = datetime.strptime(row["date_naissance"], "%Y-%m-%d").date()
                except ValueError:
                    date_naissance = None

                # Vérifier si l'email existe déjà
                if Employee.objects.filter(email=row["email"]).exists():
                    continue  # Ignore cette ligne si l'email existe déjà

                # Création de l'employé
                Employee.objects.create(
                    nom=row["nom"],
                    prenom=row["prenom"],
                    email=row["email"],
                    poste=row["poste"],
                    niveau_seniorite=row["niveau_seniorite"],
                    date_naissance=date_naissance,
                    tranche_age=row["tranche_age"],
                    date_embauche=date_embauche,
                    salaire_brut_annuel=float(row["salaire_brut_annuel"]),
                    bonus_annuel=float(row["bonus_annuel"]),
                    statut=row["statut"],
                    type_contrat=row["type_contrat"],
                    etat_civil=row["etat_civil"]
                )
                employees_created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {employees_created} employés importés avec succès !"))
