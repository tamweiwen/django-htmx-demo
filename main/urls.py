from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('notes/add', views.add_note, name='add_note'),
    path('notes/list', views.notes_list, name='notes_list'),
    path('notes/<int:pk>/edit', views.edit_note, name='edit_note'),
    path('notes/<int:pk>/remove', views.remove_note, name='remove_note')
]
