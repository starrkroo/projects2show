from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from .models import *


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('userprofile', kwargs={'username': request.user.username}))
    else:
        return redirect('login')


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
    if request.GET:
        user_search_query = request.GET.get('search-users')

        if len(user_data := User.objects.filter(username=user_search_query)) != 0:
            return redirect(reverse('userprofile', kwargs={'username': user_data[0].username}))
        else:
            return HttpResponseNotFound('<h1>Такого пользователя нет</h1>')

    context = {
        'avatar_url': User.objects.filter(username=username)[0].avatar
    }

    if request.user.username != username:
        context.update({
            'make_a_message': True
        })

    if len(user_data := User.objects.filter(username=username)) != 0:
        context.update({'user_data': user_data[0]})
        return render(request, 'users/userprofile.html', context=context)
    else:
        return HttpResponseNotFound('<h1>There is no such user</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!</h1>')


def room(request, room_id):
    username = request.user.username
    room_details = Room.objects.get(id=room_id)
    user_id = User.objects.filter(username=username)[0].id

    checki1 = Room.objects.filter(user1_id=user_id)
    checki2 = Room.objects.filter(user2_id=user_id)


    if len(checki1) or len(checki2): # if user are correct
        return redirect('/')

    return render(request, 'users/room.html', {
        'username': username,
        'room_id': room_id,
        'room_details': room_details,
    })


def checkview(request):
    user1 = request.POST['user1']
    user2 = request.POST['user2']

    user1_id = User.objects.filter(username=user1)[0].id
    user2_id = User.objects.filter(username=user2)[0].id

    checki1 = Room.objects.filter(user1_id=user1_id).filter(user2_id=user2_id)
    checki2 = Room.objects.filter(user1_id=user2_id).filter(user2_id=user1_id)

    print(len(checki1), len(checki2))

    if len(checki1) or len(checki2):
        if len(checki1):
            room_id = checki1[0].id
        else:
            room_id = checki2[0].id
        return redirect('/rooms/id' + str(room_id))
    else:
        print("MAYBE HERE???")
        user1_id = User.objects.filter(username=user1)[0].id
        user2_id = User.objects.filter(username=user2)[0].id
        Room.objects.create(user1_id=user1_id, user2_id=user2_id)
        new_room_id = Room.objects.filter(user1_id=user1_id).filter(user2_id=user2_id)[0].id
        return redirect('/rooms/id' + str(new_room_id))
        # return redirect('/'+room+'/?room_id='+str(new_room.id))


def send(request):
    print('here!!!!!!')
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room_id):
    room_details = Room.objects.get(id=room_id)

    messages = Message.objects.filter(room=room_details.id)
    # print("Found messages: " + messages)
    return JsonResponse({"messages": list(messages.values())})

