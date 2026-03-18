from django.db import models
from django.contrib.auth.models import User

class Editeur(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom de l'éditeur")
    societe = models.CharField(max_length=255, blank=True, null=True, verbose_name="Raison sociale")
    adresse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse")
    ville = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ville")
    code_postal = models.CharField(max_length=15, blank=True, null=True, verbose_name="Code Postal")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Téléphone")

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Éditeur"
        verbose_name_plural = "Éditeurs"

class Auteur(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom complet")
    annee_naissance = models.SmallIntegerField(blank=True, null=True, verbose_name="Année de naissance")

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"

class Livre(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True, verbose_name="ISBN")
    titre = models.CharField(max_length=255, verbose_name="Titre")
    annee_publication = models.SmallIntegerField(verbose_name="Année de publication")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE, verbose_name="Éditeur")
    auteurs = models.ManyToManyField(Auteur, verbose_name="Auteurs")
    est_disponible = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Client")
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, verbose_name="Livre réservé")
    date_reservation = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    est_active = models.BooleanField(default=True, verbose_name="Réservation active")

    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"