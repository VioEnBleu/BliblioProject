from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from django.contrib.auth.decorators import login_required

@login_required
def user_history_view(request):
    user_data = Reservation.objects.filter(utilisateur=request.user).order_by('-date_reservation')
    return render(request, 'user/history.html', {'reservations': user_data})

@login_required
def return_item_action(request, resa_id):
    resa = get_object_or_404(Reservation, id=resa_id, utilisateur=request.user)
    if request.method == 'POST':
        livre = resa.livre
        livre.est_disponible = True
        livre.save()
        
        resa.est_active = False
        resa.save()
        return redirect('user_history')
    return render(request, 'user/confirm_return.html', {'resa': resa})