from django.utils import timezone
from .models import Reservation

def process_return_book(resa_id):
    resa_obj = Reservation.objects.get(id=resa_id)
    if resa_obj.is_active:
        resa_obj.is_active = False
        resa_obj.save()
        
        target_item = resa_obj.book_cible
        target_item.is_dispo = True
        target_item.save()
        return True
    return False