from django.test import TestCase
from django.utils import timezone
from playapp.models import MyUser, Play, Comment, Rating, Profile

class PlayTest(TestCase):

    def setUp(self):
        self.user1 = MyUser.objects.create_user(username='admin', password='12345')
        self.play = Play.objects.create(user=self.user1, title='One', description='top', 
        image='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg', 
        download='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg')

    def test_title_play(self):
        play = Play.objects.get(id=1)
        field_play = play._meta.get_field('title').verbose_name
        self.assertEquals(field_play, 'title')

    def test_title_max_length(self):
        play = Play.objects.get(id=1)
        max_length = play._meta.get_field('title').max_length
        self.assertEquals(max_length, 35)

    def test_title_unique(self):
        play = Play.objects.get(id=1)
        unique_title = play._meta.get_field('title').verbose_name
        self.assertEquals(unique_title, 'title')

    def test_description_max_length(self):
        play = Play.objects.get(id=1)
        field_play = play._meta.get_field('description').verbose_name
        self.assertEquals(field_play, 'description')

