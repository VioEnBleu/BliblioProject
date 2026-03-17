from django.shortcuts import render, redirect, get_object_or_404
from .models import LivreItem, AuteurEntity, EditeurData
from .forms import LivreForm, AuteurForm, EditeurForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Titles

def create_livre_action(request):
    frm_obj = LivreForm(request.POST or None)
    if frm_obj.is_valid():
        frm_obj.save()
        return redirect('list_livres_admin')
    return render(request, 'admin/form_tmpl.html', {'form_data': frm_obj})

def edit_livre_action(request, item_id):
    db_item = get_object_or_404(LivreItem, isbn_id=item_id)
    frm_obj = LivreForm(request.POST or None, instance=db_item)
    if frm_obj.is_valid():
        frm_obj.save()
        return redirect('list_livres_admin')
    return render(request, 'admin/form_tmpl.html', {'form_data': frm_obj})

def delete_livre_action(request, item_id):
    db_item = get_object_or_404(LivreItem, isbn_id=item_id)
    if request.method == 'POST':
        db_item.delete()
        return redirect('list_livres_admin')
    return render(request, 'admin/confirm_del.html', {'target_obj': db_item})

@staff_member_required
def manage_books_admin(request):
    # Brigitte voit tous les livres pour les gérer
    books = Titles.objects.all()
    return render(request, 'admin/list_books.html', {'books': books})