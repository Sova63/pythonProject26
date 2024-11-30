from django.urls import path
from . import views

urlpatterns = [
    path('centre', views.centre, name='centre'),
    path('enter/', views.enter, name='enter'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('anfi/', views.anfi, name='anfi'),
]