from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import UserForm
from domain.models import User
from django.contrib import messages

def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)
            #user_email = form.cleaned_data['user_email']
            user = User.objects.filter(username=username).first()
            if user is not None and user.password == password:
                #messages.success(request, 'Успешная авторизация')
                # Сохраняем информацию о пользователе в сессию
                request.session['user_id'] = user.user_id
                request.session['username'] = user.username
                #request.session['user_email'] = user.user_email
                return redirect('index')  # Перенаправьте на нужный URL после успешной аутентификации
            else:
                messages.error(request,  'Авторизация не удалась: пароль неверный')
        else:
            messages.error(request, 'Неудачно: неверная форма')
    else:
        form = UserForm()

    return render(request, 'auth_index.html', {'form': form})


def logout(request):
    try:
        if 'user_id' in request.session:
            del request.session['user_id']
        if 'username' in request.session:
            del request.session['username']
            #del request.session['cart']
        if 'cart' in request.session:
            del request.session['cart']
    except:
        print("Error")
    return redirect('index')

