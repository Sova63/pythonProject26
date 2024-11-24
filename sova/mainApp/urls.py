from django.urls import path
from .views import cart_view,add_to_cart_movie,add_to_cart_music,add_to_cart_book, remove_from_cart, payment_page, process_payment,payment_or_signin

urlpatterns = [
    path('cart/', cart_view, name='cart_view'),
    path('add_to_cart_music/<int:pk>/', add_to_cart_music, name='add_to_cart_music'),
    path('add_to_cart_movie/<int:pk>/', add_to_cart_movie, name='add_to_cart_movie'),
    path('add_to_cart_book/<int:pk>/', add_to_cart_book, name='add_to_cart_book'),
    path('remove/<str:pk>/', remove_from_cart, name='remove_from_cart'),
    path('payment_page', payment_page, name='payment_page'),
    path('process_payment/', process_payment, name='process_payment'),
    path('check_auth/', payment_or_signin, name='check_auth'),
   ]