from django import forms
from .models import Livre, Auteur, Editeur

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['isbn', 'titre', 'annee_publication', 'editeur', 'auteurs', 'description', 'est_disponible']
        labels = {
            'isbn': 'Code ISBN',
            'titre': 'Titre du livre',
            'annee_publication': 'Année de publication',
            'editeur': 'Éditeur',
            'auteurs': 'Auteur(s)',
            'description': 'Résumé / Description',
            'est_disponible': 'Disponible en rayon',
        }
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 978-2...'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'annee_publication': forms.NumberInput(attrs={'class': 'form-control'}),
            'editeur': forms.Select(attrs={'class': 'form-control'}),
            'auteurs': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'est_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom', 'annee_naissance']
        labels = {
            'nom': 'Nom complet',
            'annee_naissance': 'Année de naissance',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'annee_naissance': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EditeurForm(forms.ModelForm):
    class Meta:
        model = Editeur
        fields = ['nom', 'societe', 'adresse', 'ville', 'code_postal', 'telephone']
        labels = {
            'nom': 'Nom de l\'éditeur',
            'societe': 'Raison sociale',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'code_postal': 'Code Postal',
            'telephone': 'Téléphone',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'societe': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'code_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }