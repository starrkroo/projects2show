from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import *
from .utils import *
from .models import *


def index(request):
    if request.GET:
        user_search_query = request.GET.get('search-users')
        data = User.objects.filter(username=user_search_query)
        context = {
            'is_searching': True,
            'user_data': 0,
            'user_query': user_search_query
        }

        if data:
            return redirect(reverse('userprofile', kwargs={'user_id': data[0].username}))

        return render(request, 'users/userprofile.html', context=context)

    context = {
        'is_searching': False,
        "title": "welcome"
    }

    return redirect(reverse('userprofile', kwargs={'username': request.user.username}))


#
# # TODO: remove the idea of using special .html file to render searching
# # SOLUTION: you can easily connect query with searching account
# def searching_page(request):
#     search_user_name = request.GET.get('search-users')
#     found_user = User.objects.filter(username=search_user_name)[0]
#     return render(request, 'users/searching_page.html', context={"found_user": found_user})


class LoginUser(LoginView):
    form_classes = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('userprofile', kwargs={'username': user.username}))


def logout_user(request):
    logout(request)
    return redirect('login')


def show_user_profile(request, username):
    # логика при поиске через форму
    if request.GET:
        user_search_query = request.GET.get('search-users')
        # проверка по урлу и по непосредственно запросу

        if len(user_data := User.objects.filter(username=user_search_query)) != 0:
            return redirect(reverse('userprofile', kwargs={'username': user_data[0].username}))
        else:
            return HttpResponseNotFound('<h1>Такого пользователя нет</h1>')

    # логика при поиске через ввод в строку маршрутизации
    if len(user_data := User.objects.filter(username=username)) != 0:
        return render(request, 'users/userprofile.html', context={'user_data': user_data[0]})
    else:
        return HttpResponseNotFound('<h1>Такого пользователя нет</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
