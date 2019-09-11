from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


def login(request):
    """Зарегестрировать вход в систему"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Доступ разрешен!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Не правильно введены имя пользователя или пароль')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """Выход для авторизованного пользователя"""
    auth.logout(request)
    return redirect('/accounts/dashboard')


def register(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                # Кинуть в error massage, что пользователь существует
                messages.error(request, 'Пользователь с таким именем уже существует')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # Кинуть в error massage, email уже кем то занят
                messages.error(request, 'Email уже занят другим пользователем')
                return redirect('register')
            else:
                # Создаем нового пользователя
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Ваш аккаунт зарегестрирован. Теперь можете осуществить вход')
                return redirect('login')
        else:
            # Если пароли не совпадают, кидаем ошибку и, желательно показывать
            # форму с уже заполнеными полями login и email
            messages.error(request, 'Введеный вами пароли не совпадают')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    """Личный кабинет пользователя"""
    return render(request, 'accounts/dashboard.html')
