# Generated by Django 5.1.6 on 2025-02-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='etat_civil',
            field=models.CharField(blank=True, choices=[('Célibataire', 'Célibataire'), ('Marié(e)', 'Marié(e)'), ('Divorcé(e)', 'Divorcé(e)'), ('Veuf/Veuve', 'Veuf/Veuve')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='tranche_age',
            field=models.CharField(blank=True, choices=[('20-30', '20-30'), ('30-40', '30-40'), ('40-50', '40-50'), ('50-62', '50-62')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='type_contrat',
            field=models.CharField(blank=True, choices=[('CIVP', 'CIVP'), ('CDD', 'CDD'), ('CDI', 'CDI'), ('Alternance', 'Alternance'), ('Stage', 'Stage')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='statut',
            field=models.CharField(choices=[('Actif', 'Actif'), ('Conge', 'Conge')], max_length=50),
        ),
    ]
