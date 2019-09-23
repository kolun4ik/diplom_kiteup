from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Profile
from .forms import ProfileForm



class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'


class SignupFormView(FormView):

    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = 'accounts/login'

    def form_valid(self, form):
        form.save()
        return super(SignupFormView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    # fields = ['avatar',]
    template_name = 'accounts/profile.html'


# def register(request):
#     """Регистрация нового пользователя"""
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#
#         if password == password2:
#             if User.objects.filter(username=username).exists():
#                 # Кинуть в error massage, что пользователь существует
#                 messages.error(request, 'Пользователь с таким именем уже существует')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 # Кинуть в error massage, email уже кем то занят
#                 messages.error(request, 'Email уже занят другим пользователем')
#                 return redirect('register')
#             else:
#                 # Создаем нового пользователя
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()
#                 messages.success(request, 'Ваш аккаунт зарегестрирован. Теперь можете осуществить вход')
#                 return redirect('login')
#         else:
#             # Если пароли не совпадают, кидаем ошибку и, желательно показывать
#             # форму с уже заполнеными полями login и email
#             messages.error(request, 'Введеный вами пароли не совпадают')
#             return redirect('register')
#     else:
#         return render(request, 'accounts/register.html')
#
#
# def dashboard(request):
#     """Личный кабинет пользователя"""
#     return render(request, 'accounts/dashboard.html')
