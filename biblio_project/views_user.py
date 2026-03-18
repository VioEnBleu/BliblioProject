from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre, Reservation
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def list_all_books_view(request):
    data_qs = Livre.objects.all()
    return render(request, 'user/list.html', {'items_list': data_qs})

def search_engine_req(request):
    query_str = request.GET.get('q', '')
    # Utilisation des nouveaux champs 'titre' au lieu de 'title_nom'
    results_qs = Livre.objects.filter(
        Q(titre__icontains=query_str) |
        Q(isbn__icontains=query_str)
    )
    return render(request, 'user/list.html', {'items_list': results_qs})

def book_detail_view(request, item_id):
    # Utilisation de 'isbn' au lieu de 'isbn_id'
    book_obj = get_object_or_404(Livre, isbn=item_id)
    return render(request, 'user/detail.html', {'book': book_obj})

@login_required
def book_resa_action(request, book_id):
    # Utilisation de 'isbn' au lieu de 'isbn_id'
    target_book = get_object_or_404(Livre, isbn=book_id)
    user_current = request.user
    
    # Utilisation de 'utilisateur' et 'est_active'
    count_active = Reservation.objects.filter(
        utilisateur=user_current, 
        est_active=True
    ).count()
    
    # Utilisation de 'est_disponible', 'utilisateur' et 'livre'
    if count_active < 5 and target_book.est_disponible:
        Reservation.objects.create(
            utilisateur=user_current, 
            livre=target_book
        )
        target_book.est_disponible = False
        target_book.save()
        
    return redirect('user_history')