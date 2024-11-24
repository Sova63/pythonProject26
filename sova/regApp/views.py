from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from domain.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError


def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			if User.objects.filter(username=username).exists():
				messages.error(request,"Пользователь с таким именем уже существует.")
			else:
				form.save()
				messages.success(request, "Регистрация прошла успешно!")
				return redirect('signup')
	else:
		form = UserForm()
	return render(request,'reg_index.html',{'form': form})





