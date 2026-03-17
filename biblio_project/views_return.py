from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BookingResa
from .services_logic import process_return_book


@login_required
def user_history_view(request):
    user_data = BookingResa.objects.filter(user_client=request.user).order_by('-date_creation')
    return render(request, 'user/history.html', {'history_items': user_data})

def return_item_action(request, resa_id):
    if request.method == 'POST':
        process_return_book(resa_id)
    return redirect('user_history')