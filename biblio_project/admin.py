from django.contrib import admin
from .models import Editeur, Auteur, Livre, Reservation

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'isbn', 'annee_publication', 'est_disponible')
    list_filter = ('est_disponible', 'editeur')
    search_fields = ('titre', 'isbn')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'livre', 'date_reservation', 'est_active')
    list_filter = ('est_active',)

admin.site.register(Editeur)
admin.site.register(Auteur)