import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView , DetailView , View, TemplateView
from .models import Play, MyUser, Comment, Rating, Profile
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CreateGameForm, CommentCreateForm, RatingPlayCreateForm, TopRatingPlayGetForm
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Avg, Q
from django.conf import settings


class MainView(ListView):
    model = Play
    template_name = 'index.html'
    extra_context = {'top': TopRatingPlayGetForm}
    
    def get_queryset(self):
        self.paginate_by = 9
        if 'top' in self.request.GET:
            return Play.objects.annotate(average_rating=Avg('plays_rating__rating')).order_by('-average_rating')
        return Play.objects.annotate(average_rating=Avg('plays_rating__rating'))


class SearchResultsView(ListView):
    model = Play
    template_name = 'search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Play.objects.filter(
            Q(title__icontains=query) 
        )
        return object_list

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


class ListPlayView(DetailView):
    model = Play
    template_name = 'Game.html'
    slug_url_kwarg = 'title'
    slug_field = 'title'

    def get_queryset(self):
        return Play.objects.annotate(average_rating=Avg('plays_rating__rating'))


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

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="plays/download")
            response['Content-Disposition'] = 'inline; filename' + os.path.basename(file_path)
            return response
  
    raise Http404

class ProfileUserView(DetailView):
    model = MyUser
    template_name = 'profile.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'



