from django.shortcuts import render, redirect,get_object_or_404
from .models import Order,User
import time
from django.db.models import Max
from .forms import ProfileForm,PasswordChangeForm
#from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from domain.models import User
from feedback.forms import EntryForm
from feedback.models import Entry
def download_page(request):
    # Получаем ID текущего пользователя из сессии
    user_id = request.session.get('user_id')

    # Получаем максимальную дату для текущего пользователя
    max_date = Order.objects.filter(user_id=user_id).aggregate(max_date=Max('date'))['max_date']

    if max_date:
        # Преобразуем max_date в datetime, если это строка
        if isinstance(max_date, str):
            max_date = timezone.datetime.fromisoformat(max_date)

        # Рассчитываем дату 10 секунд назад от max_date
        time_threshold = max_date - timedelta(seconds=10)

        # Получаем все заказы для текущего пользователя за последние 10 секунд
        latest_orders = Order.objects.filter(user_id=user_id, date__gte=time_threshold, date__lte=max_date)
    else:
        latest_orders = []  # Если нет заказов, возвращаем пустой список

    return render(request, 'download_page.html', {'products': latest_orders})


'''def account(request):
    # Получаем ID текущего пользователя из сессии
    user_id = request.session.get('user_id')
    if user_id is None:
        # Обработка случая, если пользователь не авторизован
        return render(request, 'download_page.html', {'products': []})

    # Получаем все заказы для текущего пользователя
    latest_orders = Order.objects.filter(user_id=user_id)
    user = User.objects.get(user_id=user_id)
    #print(user.username)
    return render(request, 'account.html', {'products': latest_orders,"user_info":user})'''

'''def centre(request):
    entries = Entry.objects.all()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centre')
    else:
        form = EntryForm()
    return render(request, 'account.html', {'form': form,'entries': entries})'''

def account(request):
    # Получаем ID текущего пользователя из сессии
    user_id = request.session.get('user_id')
    if user_id is None:
        # Обработка случая, если пользователь не авторизован
        return render(request, 'download_page.html', {'products': []})

    # Получаем все заказы для текущего пользователя
    latest_orders = Order.objects.filter(user_id=user_id)
    user = User.objects.get(user_id=user_id)

    # Получаем все отзывы пользователя
    entries = Entry.objects.filter(diary_id=user_id)

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = EntryForm()

    return render(request, 'account.html', {
        'products': latest_orders,
        'user_info': user,
        'form': form,
        'entries': entries
    })


def start_download(request):
    # Имитация процесса скачивания
    for i in range(3, -1, -1):
        time.sleep(1)
    return render(request, 'download_complete.html')



def profile_view(request):
    user_id = request.session.get('user_id')
    
    user = get_object_or_404(User, user_id=request.session.get('user_id'))
    profile_form = ProfileForm(instance=user)
    password_form = PasswordChangeForm(instance=user)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=user)
        password_form = PasswordChangeForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
        if password_form.is_valid():
            password_form.save()
        return redirect("account")

    latest_orders = Order.objects.filter(user_id=user_id)
    user = User.objects.get(user_id=user_id)

    context = {
        'user_info': user,
        'products': latest_orders,
        'user': user,
        'profile_form': profile_form,
        'password_form': password_form,
        # Add any other context variables you need here
    }

    return render(request, 'account.html', context)