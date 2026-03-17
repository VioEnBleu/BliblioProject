from django import forms
from .models import LivreItem, AuteurEntity, EditeurData, Titles

class LivreForm(forms.ModelForm):
    class Meta:
        model = LivreItem
        fields = '__all__'

class AuteurForm(forms.ModelForm):
    class Meta:
        model = AuteurEntity
        fields = '__all__'

class EditeurForm(forms.ModelForm):
    class Meta:
        model = EditeurData
        fields = '__all__'
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Titles
        fields = ['isbn', 'title', 'year_published', 'author_id', 'pub_id', 'description']
        labels = {
            'isbn': 'Code ISBN',
            'title': 'Titre du livre',
            'year_published': 'Année de publication',
            'author_id': 'Auteur',
            'pub_id': 'Éditeur',
            'description': 'Résumé / Description',
        }
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 978-2...'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year_published': forms.NumberInput(attrs={'class': 'form-control'}),
            'author_id': forms.Select(attrs={'class': 'form-control'}),
            'pub_id': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }