from django.urls import path
from .views import *
urlpatterns = [
	path('sign-up',signup,name="signup"),
]