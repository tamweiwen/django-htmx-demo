from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('notes/add', views.add_note, name='add_note')
]
