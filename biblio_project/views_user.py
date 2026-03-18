from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre, Reservation
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def list_all_books_view(request):
    data_qs = Livre.objects.all()
    return render(request, 'user/list.html', {'items_list': data_qs})

def search_engine_req(request):
    query_str = request.GET.get('q', '')
    results_qs = Livre.objects.filter(
        Q(title_nom__icontains=query_str) |
        Q(sujet_topic__icontains=query_str)
    )
    return render(request, 'user/list.html', {'items_list': results_qs})

def book_detail_view(request, item_id):
    book_obj = get_object_or_404(Livre, isbn_id=item_id)
    return render(request, 'user/detail.html', {'book': book_obj})

@login_required
def book_resa_action(request, book_id):
    target_book = get_object_or_404(Livre, isbn_id=book_id)
    user_current = request.user
    
    count_active = Reservation.objects.filter(
        user_client=user_current, 
        is_active=True
    ).count()
    
    if count_active < 5 and target_book.is_dispo:
        Reservation.objects.create(
            user_client=user_current, 
            book_cible=target_book
        )
        target_book.is_dispo = False
        target_book.save()
        
    return redirect('user_history')