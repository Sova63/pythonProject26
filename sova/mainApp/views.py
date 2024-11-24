from django.shortcuts import render, redirect,get_object_or_404
from .models import Product
from .forms import AddToCartForm
from intshop.models import Product_movie,Product_music,Product_book,Category_product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from load.models import Order
from django.utils import timezone
from domain.models import User
from datetime import datetime

def get_cart(request):
    return request.session.get('cart', {})

def update_cart(request, cart):
    request.session['cart'] = cart

def add_to_cart(request, pk, product_model):
    product = product_model.objects.get(pk=pk)

    cart = get_cart(request)

    # Создаем словарь для сопоставления английских названий категорий с русскими
    category_translation = {
        'Music': 'Музыка',
        'Movie': 'Фильм',
        'Books': 'Книга'
    }

    # Получаем русское название категории
    category_name_ru = category_translation.get(product.category.category_name, product.category.category_name)
    cart_key = str(pk) + '-' + category_name_ru

    # Обновляем корзину с русскими названиями категорий
    cart[cart_key] = {
        'pk': pk,
        'image': product.image,
        'name': product.name,
        'price': str(product.price),
        'category': category_name_ru,  # Используем русское название категории
        'category_id':product.category_id,
        'quantity': 1  # Начальное количество
    }
    update_cart(request, cart)

    if product.category.category_name == 'Music':
        return redirect('music')
    elif product.category.category_name == 'Movie':
        return redirect('movie')
    elif product.category.category_name == 'Books':
        return redirect('book')
    else:
        return redirect('index')

def remove_from_cart(request, pk):
    cart = get_cart(request)
    if str(pk) in cart:
        del cart[str(pk)]
    update_cart(request, cart)
    return redirect('cart_view')

def cart_view(request):
    cart = get_cart(request)
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    total_quantity = sum(item['quantity'] for item in cart.values())
    cart_count = len(request.session.get('cart', []))    # Получаем количество товаров из сессии

    return render(request, 'cart.html', {'cart': cart, 'total': total, 'total_quantity': total_quantity, 'cart_count': cart_count})

def add_to_cart_music(request, pk):
    return add_to_cart(request, pk, Product_music)
def add_to_cart_movie(request, pk):
    return add_to_cart(request, pk, Product_movie)
def add_to_cart_book(request, pk):
    return add_to_cart(request, pk, Product_book)

def payment_page(request):
    cart = get_cart(request)
    total = sum(float(item['price']) for item in cart.values())
    return render(request, 'payment.html', {'total': total})

def process_payment(request):
    if request.method == 'POST':
        #cart = get_cart(request)
        cart = request.session.get('cart', {})
        user =  request.session['user_id']# Предполагается, что пользователь авторизован

        #print(user)
       #print(cart)
        for item in cart.values():
            # Проверяем наличие необходимых ключей в item
            product_type = item.get('category')  # Используем get для безопасного получения значения
            product_id = item.get('pk')
            category_id = item.get('category_id')

            #print(product_type, product_id)
            if product_type is None or product_id is None:  # Проверяем, что ключи существуют
                continue  # Если нет, пропускаем текущую итерацию

            if product_type == 'Фильм':
                product = product_id
            elif product_type == 'Книга':
                product = product_id
            elif product_type == 'Музыка':
                product = product_id
            else:
                continue

            order = Order.objects.create(
                user_id_id=user,  # Исправлено получение пользователя
                movie_id_id=product if product_type == 'Фильм' else None,
                book_id_id=product if product_type == 'Книга' else None,
                music_id_id=product if product_type == 'Музыка' else None,
                category_id=category_id,
                date=datetime.now()

            )
        # Очистка корзины после создания заказа
        request.session['cart'] = {}

        return render(request, 'paynew.html')  # Перенаправление на страницу успешного платежа

    return redirect('payment_page')  # Если метод не POST, перенаправление на страницу оплаты


def payment_or_signin(request):
    # Проверяем, авторизован ли пользователь
    if 'username' in request.session:
        # Если пользователь авторизован, перенаправляем на страницу оплаты
        return redirect('payment_page')
    else:
        # Если пользователь не авторизован, выводим сообщение и перенаправляем на страницу авторизации
        messages.error(request, 'Необходимо авторизоваться для доступа к странице оплаты.')
        return redirect('signin')





