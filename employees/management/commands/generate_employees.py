import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialiser Faker pour générer des données aléatoires
fake = Faker()

# Définition des choix possibles
POSTES = ["IT Engineer", "Business Analyst", "Project Manager", "Cloud Specialist", "Data Scientist"]
NIVEAUX_SENIORITE = ["Junior", "Mid", "Senior", "Lead"]
STATUTS = ["Active", "Conge"]
CONTRATS = ["CIVP", "CDD", "CDI", "Alternance", "Stage"]
ETAT_CIVIL = ["Célibataire", "Marié(e)", "Divorcé(e)", "Veuf(ve)"]
AGE_RANGES = {
    "20-30": (20, 30),
    "30-40": (30, 40),
    "40-50": (40, 50),
    "50-62": (50, 62)
}

# Fonction pour générer une date de naissance et la tranche d'âge associée
def generer_date_naissance_et_tranche():
    tranche = random.choice(list(AGE_RANGES.keys()))
    age_min, age_max = AGE_RANGES[tranche]
    date_naissance = fake.date_of_birth(minimum_age=age_min, maximum_age=age_max)
    return date_naissance, tranche

# Générer le fichier CSV avec 1000 employés
file_path = "employes_IT.csv"

with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "nom", "prenom", "email", "poste", "niveau_seniorite", 
        "date_naissance", "tranche_age", "date_embauche", 
        "salaire_brut_annuel", "bonus_annuel", "statut", "type_contrat", "etat_civil"
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Ajouter l'en-tête du fichier CSV

    for _ in range(1000):  # Générer 1000 employés
        date_naissance, tranche_age = generer_date_naissance_et_tranche()
        
        writer.writerow({
            "nom": fake.last_name(),
            "prenom": fake.first_name(),
            "email": fake.email(),
            "poste": random.choice(POSTES),
            "niveau_seniorite": random.choice(NIVEAUX_SENIORITE),
            "date_naissance": date_naissance.strftime("%Y-%m-%d"),
            "tranche_age": tranche_age,
            "date_embauche": fake.date_this_century().strftime("%Y-%m-%d"),
            "salaire_brut_annuel": round(random.uniform(30000, 120000), 2),
            "bonus_annuel": round(random.uniform(2000, 10000), 2),
            "statut": random.choice(STATUTS),
            "type_contrat": random.choice(CONTRATS),
            "etat_civil": random.choice(ETAT_CIVIL)
        })

print(f"✅ Fichier CSV généré avec 1000 employés à {file_path} !")
