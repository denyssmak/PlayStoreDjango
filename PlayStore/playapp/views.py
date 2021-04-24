from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView , DetailView , View, TemplateView
from .models import Play, MyUser, Comment, Rating
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CreateGameForm, CommentCreateForm, RatingPlayCreateForm
from django.contrib.auth.views import LoginView, LogoutView


class MainView(ListView):
    model = Play
    template_name = 'index.html'


class RegisterUserView(CreateView):
    model = MyUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


class MyloginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return self.success_url


class MyUserlogoutView(LogoutView):
    next_page = reverse_lazy('index')


class CreateGameView(CreateView):
    template_name = 'create_game.html'
    form_class = CreateGameForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        return super().form_valid(form=form)

class ListGameView(ListView):
    model = Play
    template_name = 'list_game.html'
    success_url = reverse_lazy('index')


class ListPlayView(DetailView):
    model = Play
    template_name = 'Game.html'
    slug_url_kwarg = 'title'
    slug_field = 'title'
    success_url = reverse_lazy('Game')

class CommentPlayView(TemplateView):
    model = Comment
    template_name = 'Game.html'


class CommentCreatePlayView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentCreateForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        pk = self.kwargs['pk']
        play = Play.objects.get(id=pk)
        object.play = play
        object.save()
        return super().form_valid(form=form)

    def get_success_url(self):
        titles = self.object.play.title
        return reverse('Game', kwargs={'title': titles})

class RatingPlayCreateView(CreateView):
    model = Rating
    template_name = 'rating_create.html'
    form_class = RatingPlayCreateForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        pk = self.kwargs['pk']
        play = Play.objects.get(id=pk)
        object.play = play
        object.save()
        return super().form_valid(form=form)

    def get_success_url(self):
        titles = self.object.play.title
        return reverse('Game', kwargs={'title': titles})