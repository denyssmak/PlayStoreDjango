from django.urls import path, include
from playapp.views import registerview, MainView, MyloginView, ListGameView, MyUserlogoutView, CreateGameView, ListPlayView, CommentCreatePlayView, RatingPlayCreateView, ProfileUserView, SearchResultsView
import os
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login/', MyloginView.as_view(), name='login_page'),
    path('register/', registerview, name='register_page'),
    path('logout/', MyUserlogoutView.as_view(), name='logout_page'),
    path('create_game/', CreateGameView.as_view(), name='create_game'),
    path('list_game/', ListGameView.as_view(), name='list_game'),
    path('Game/<str:title>/', ListPlayView.as_view(), name='Game'),
    path('comment_create/<int:pk>/',
         CommentCreatePlayView.as_view(), name='comment_create'),
    path('rating_create/<int:pk>/',
         RatingPlayCreateView.as_view(), name='rating_create'),
    path(r'^download/(?P<path>.*)$', serve,
         {'document_root': settings.MEDIA_ROOT}),
    path('profile/<str:username>/', ProfileUserView.as_view(), name='profile'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
