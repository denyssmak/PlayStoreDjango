from django.urls import path, include
from playapp.views import MainView, MyloginView, RegisterUserView, ListGameView, MyUserlogoutView, CreateGameView, ListPlayView, CommentCreatePlayView, RatingPlayCreateView                          

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('login/', MyloginView.as_view(), name='login_page'),
    path('register/', RegisterUserView.as_view(), name='register_page'),
    path('logout/', MyUserlogoutView.as_view(), name='logout_page'),
    path('create_game/', CreateGameView.as_view(), name='create_game'),
    path('list_game/', ListGameView.as_view(), name='list_game'),
    path('Game/<str:title>/', ListPlayView.as_view(), name='Game'),
    path('comment_create/<int:pk>/' , CommentCreatePlayView.as_view(), name='comment_create'),
    path('rating_create/<int:pk>/', RatingPlayCreateView.as_view(), name='rating_create')
]
