from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
	path('movie', views.movie, name='movie'),
	path('viewing_movie/<int:pk>/', views.viewing_movie, name='viewing_movie'),
	path('book', views.book, name='book'),
	path('viewing_book/<int:pk>/', views.viewing_book, name='viewing_book'),
	path('music', views.music, name='music'),
	path('viewing_music/<int:pk>/', views.viewing_music, name='viewing_music'),
	path('search_results', views.search_results, name='search_results')
]