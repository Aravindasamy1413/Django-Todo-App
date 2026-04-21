from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),#homepage complete url

    path('notes/',notes,name='notes'),

    path('edit-note/<int:id>',edit_note,name='edit_note'),

    path('delete-note/<int:id>',delete_note,name='delete_note'),

    path('trash/',trash,name='trash'),



    path('complete_/<int:id>',complete_,name='complete_'),#homepage complete button url

    path('delete_/<int:id>',delete_,name='delete_'),#home page delete button

    path('complete_delete_all/',complete_delete_all,name='complete_delete_all'),

    path('complete_delete/<int:id>', complete_delete, name='complete_delete'), #complete page delete button

    path('complete_all/',complete_all,name='complete_all'),#home page com
    
    path('delete_all/',delete_all,name='delete_all'),

    path('update/<int:id>',update,name='update'),

    path('crestore/<int:id>',crestore,name='crestore'), #complete page restore button

    path('crestore_all',crestore_all,name='crestore_all'),

    path('trash_delete/<int:id>',trash_delete,name='trash_delete'), #trash page delete button

    path('trash_delete_all/',trash_delete_all,name='trash_delete_all'),

    path('trash_restore/<int:id>',trash_restore,name='trash_restore'), #trash page restore button

    path('trash_restore_all/',trash_restore_all,name='trash_restore_all'),

    path('register/',register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),

    path('forgot-password/',forgot_password,name='forgot_password'),

    path('reset-password/', reset_password, name='reset_password'),
]
