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
                # Convertir la date d'embauche
                try:
                    date_embauche = datetime.strptime(row["date_embauche"], "%Y-%m-%d").date()
                except ValueError:
                    date_embauche = None

                # Création de l'employé
                Employee.objects.create(
                    nom=row["nom"],
                    prenom=row["prenom"],
                    email=row["email"],
                    poste=row["poste"],
                    niveau_seniorite=row["niveau_seniorite"],
                    date_embauche=date_embauche,
                    salaire_brut_annuel=float(row["salaire_brut_annuel"]),
                    bonus_annuel=float(row["bonus_annuel"]),
                    statut=row["statut"]
                )
                employees_created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {employees_created} employés importés avec succès !"))
