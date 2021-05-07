from django.test import TestCase
from playapp.models import MyUser, Play, Comment, Rating, Profile
from playapp.forms import CreateGameForm, CommentCreateForm, RatingPlayCreateForm, TopRatingPlayGetForm

class CreateGameFormTest(TestCase):

    def setUp(self):
        self.user1 = MyUser.objects.create_user(username='admin', password='12345')
        self.play = Play.objects.create(user=self.user1, title='One', description='top', 
        image='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg', 
        download='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg')


    # def test_create_play(self):
    #     form_data = {'title':'a', 'description':'top', 'image':self.image, 'download':self.download}
    #     form = CreateGameForm(data=form_data)
    #     self.assertTrue(form.is_valid())

class CommentCreateFormTest(TestCase):

    def setUp(self):
        self.user1 = MyUser.objects.create_user(username='admin', password='12345')
        self.play = Play.objects.create(user=self.user1, title='One', description='top', 
        image='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg', 
        download='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg')

    def test_create_comment(self):
        form_data = {'content':'bla'}
        form = CommentCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

class RatingPlayCreateFormTest(TestCase):

    def setUp(self):
        self.user1 = MyUser.objects.create_user(username='admin', password='12345')
        self.play = Play.objects.create(user=self.user1, title='One', description='top', 
        image='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg', 
        download='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg')

    def test_create_rating(self):
        form_data = {'rating':1}
        form = RatingPlayCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_rating_false(self):
        form_data = {'rating':10}
        form = RatingPlayCreateForm(data=form_data)
        self.assertFalse(form.is_valid())