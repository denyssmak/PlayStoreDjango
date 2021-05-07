from django.test import TestCase
from django.utils import timezone
from playapp.models import MyUser, Play, Comment, Rating, Profile
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from playapp.forms import CustomUserCreationForm

class UserLoginViewTest(TestCase):

    def setUp(self):
        self.data = {'username': 'admin', 'password': '123'}
        self.user = MyUser.objects.create_user(**self.data)
        self.url = reverse('login_page')

    def test_user_login_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.failUnless(isinstance(response.context['form'], AuthenticationForm))

    def test_user_login_post_succes_redirect(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('index'))

    def test_user_login_post(self):
        data = {'username': 'admin', 'password': '7weds'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())


class UserRegisterViewTest(TestCase):

    def setUp(self):
        self.url = reverse('register_page')
        self.data = {'username': 'admin', 'password1': '123', 'password2': '123'}

    def test_user_register_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.failUnless(isinstance(response.context['form'], CustomUserCreationForm))

    def test_user_register_post_succes(self):
        response = self.client.post(self.url, data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MyUser.objects.count(), 1)

    def test_user_register_post_redirect(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('index'))

    def test_user_register_post_failure(self):
        data = {'username': 'admin', 'password1': '1df2q', 'password2': 'offfw3'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MyUser.objects.count(), 0)
        self.assertFalse(response.context['form'].is_valid())
        self.assertTrue(response.context['form'].errors)


class UserLogoutView(TestCase):

    def setUp(self):
        self.user = MyUser.objects.create_user(username='admin', password='123')
        self.client.force_login(self.user)
        self.url = reverse('logout_page')

    def test_user_logout_get(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_user_logout_get_redirect(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('index'))

class MainViewTest(TestCase):

    def setUp(self):
        self.user1 = MyUser.objects.create_user(username='admin', password='123')
        self.play = Play.objects.create(user=self.user1, title='One', description='top', 
                                        image='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg', 
                                        download='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg')
        self.url = reverse('index')
    
    def test_url(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')