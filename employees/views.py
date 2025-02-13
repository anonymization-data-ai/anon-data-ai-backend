from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from employees.models import Employee
from django.db.models import Avg, Count

@api_view(['GET'])
def employee_stats(request):
    # Nombre total d'employés
    total_employes = Employee.objects.count()

    # Salaires moyens par poste
    salaires_par_poste = Employee.objects.values("poste").annotate(salaire_moyen=Avg("salaire_brut_annuel"))
    salaires_stats_poste = {item["poste"]: round(item["salaire_moyen"], 2) for item in salaires_par_poste}

    # Salaires moyens par niveau de séniorité
    salaires_par_seniorite = Employee.objects.values("niveau_seniorite").annotate(salaire_moyen=Avg("salaire_brut_annuel"))
    salaires_stats_seniorite = {item["niveau_seniorite"]: round(item["salaire_moyen"], 2) for item in salaires_par_seniorite}

    # Répartition des postes
    postes_counts = Employee.objects.values("poste").annotate(total=Count("poste"))
    postes_stats = {item["poste"]: item["total"] for item in postes_counts}

    # Répartition des niveaux de séniorité
    niveaux_counts = Employee.objects.values("niveau_seniorite").distinct().count()

    # Répartition des statuts
    statuts_counts = Employee.objects.values("statut").annotate(total=Count("statut"))
    statuts_stats = {item["statut"]: item["total"] for item in statuts_counts}

    # Répartition par tranche d'âge
    tranche_age_counts = Employee.objects.values("tranche_age").annotate(total=Count("tranche_age"))
    tranche_age_stats = {item["tranche_age"]: item["total"] for item in tranche_age_counts}

    # Répartition par type de contrat
    type_contrat_counts = Employee.objects.values("type_contrat").annotate(total=Count("type_contrat"))
    type_contrat_stats = {item["type_contrat"]: item["total"] for item in type_contrat_counts}

    # Répartition par état civil
    etat_civil_counts = Employee.objects.values("etat_civil").annotate(total=Count("etat_civil"))
    etat_civil_stats = {item["etat_civil"]: item["total"] for item in etat_civil_counts}

    # Salaire moyen global
    salaire_moyen = Employee.objects.aggregate(Avg("salaire_brut_annuel"))["salaire_brut_annuel__avg"]

    # Construction de la réponse
    data = {
        "Nombre total d'employés": total_employes,
        "Nombre de postes différents": len(postes_stats),
        "Répartition des niveaux de séniorité": niveaux_counts,
        "Répartition des statuts": statuts_stats,
        "Répartition par tranche d'âge": tranche_age_stats,
        "Répartition par type de contrat": type_contrat_stats,
        "Répartition par état civil": etat_civil_stats,
        "Salaire moyen global": round(salaire_moyen, 2) if salaire_moyen else 0,
        "Nombre d'employés par spécialité": postes_stats,
        "Salaires moyens par poste": salaires_stats_poste,  
        "Salaires moyens par niveau de séniorité": salaires_stats_seniorite,  
    }

    return Response(data)
