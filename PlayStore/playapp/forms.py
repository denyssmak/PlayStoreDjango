from .models import Play, MyUser, Comment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = MyUser
		fields = ('username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
	class Meta:
		model = MyUser
		fields = ('username', 'password')

class CreateGameForm(forms.ModelForm):
	class Meta:
		model = Play
		fields = ('title', 'description', 'image', )

class CommentCreateForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)