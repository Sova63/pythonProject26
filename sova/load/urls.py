from django.urls import path
from . import views
from .views import account, profile_view

urlpatterns = [
    path('download_page', views.download_page, name='download_page'),
    path('start_download', views.start_download, name='start_download'),
    path('account', views.account, name='account'),
    path('profile_view', views.profile_view, name='profile_view'),
]