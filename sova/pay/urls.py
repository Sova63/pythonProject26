from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_page, name='payment_page'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('paynew/', views.paynew, name='paynew'),
    path('index', index, name='index'),
    path('download_page', views.download_page, name='download_page'),
]