from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from load.models import Order
'''def process_payment(request):
    if request.method == 'POST':
        # Обработка данных формы
        bank = request.POST.get('bank')
        card_number = request.POST.get('card_number')
        card_expiry = request.POST.get('card_expiry')
        card_cvv = request.POST.get('card_cvv')
        sms_code = request.POST.get('sms_code')

        # Здесь можно добавить логику обработки платежа
        return HttpResponse("Платеж успешно обработан!")
    return redirect('payment_page')'''


'''def process_payment(request):
    if request.method == 'POST':
        # Обработка данных формы
        bank = request.POST.get('bank')
        card_number = request.POST.get('card_number')
        card_expiry = request.POST.get('card_expiry')
        card_cvv = request.POST.get('card_cvv')
        sms_code = request.POST.get('sms_code')

        # Возвращаем HTML с кнопками
        return render(request, 'paynew.html')
    return redirect('payment_page')'''

'''def download_page(request):
    products = Order.objects.all()
    return render(request, 'download_page.html', {'products': products})'''