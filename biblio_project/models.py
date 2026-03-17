from django.db import models
from django.contrib.auth.models import User

class EditeurData(models.Model):
    name_str = models.CharField(max_length=50)
    societe_nom = models.CharField(max_length=255, blank=True, null=True)
    adresse_loc = models.CharField(max_length=50, blank=True, null=True)
    city_ville = models.CharField(max_length=20, blank=True, null=True)
    state_prov = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    tel_num = models.CharField(max_length=15, blank=True, null=True)
    fax_num = models.CharField(max_length=15, blank=True, null=True)
    infos_text = models.TextField(blank=True, null=True)

class AuteurEntity(models.Model):
    nom_author = models.CharField(max_length=50)
    birth_annee = models.SmallIntegerField(blank=True, null=True)

class LivreItem(models.Model):
    isbn_id = models.CharField(max_length=20, primary_key=True)
    title_nom = models.CharField(max_length=255)
    pub_year = models.SmallIntegerField(blank=True, null=True)
    desc_text = models.CharField(max_length=50, blank=True, null=True)
    notes_str = models.CharField(max_length=50, blank=True, null=True)
    sujet_topic = models.CharField(max_length=50, blank=True, null=True)
    details_txt = models.TextField(blank=True, null=True)
    editeur_link = models.ForeignKey(EditeurData, on_delete=models.CASCADE)
    auteurs_rel = models.ManyToManyField(AuteurEntity)
    is_dispo = models.BooleanField(default=True)

class BookingResa(models.Model):
    user_client = models.ForeignKey(User, on_delete=models.CASCADE)
    book_cible = models.ForeignKey(LivreItem, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    from django.db import models

class Authors(models.Model):
    au_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    year_born = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.author

class Publishers(models.Model):
    pubid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Titles(models.Model):
    isbn = models.CharField(primary_key=True, max_length=20) 
    title = models.CharField(max_length=255) 
    year_published = models.SmallIntegerField() 
    description = models.TextField(null=True, blank=True)
    pub_id = models.ForeignKey(Publishers, on_delete=models.CASCADE) 
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return self.title