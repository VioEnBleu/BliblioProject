from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView 
from biblio_project import views_admin, views_user, views_return
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(url='catalogue/', permanent=True)),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('admin/books/add/', views_admin.create_livre_action, name='add_book'),
    path('admin/books/edit/<str:item_id>/', views_admin.edit_livre_action, name='edit_book'),
    path('admin/books/delete/<str:item_id>/', views_admin.delete_livre_action, name='del_book'),
    path('catalogue/', views_user.list_all_books_view, name='list_books'),
    path('search/', views_user.search_engine_req, name='search_books'),
    path('reserve/<str:book_id>/', views_user.book_resa_action, name='reserve_book'),
    path('my-books/', views_return.user_history_view, name='user_history'),
    path('return/<int:resa_id>/', views_return.return_item_action, name='return_book'),
]