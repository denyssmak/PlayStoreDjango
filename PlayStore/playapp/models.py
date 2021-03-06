from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
import os
from django.conf import settings

IMPORTANCE_CHOICE = ((1, 1),
                     (2, 2),
                     (3, 3),
                     (4, 4),
                     (5, 5))


class MyUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Play(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='players')
    title = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=120)
    image = models.ImageField()
    date_published = models.DateField(auto_now=True)
    download = models.FileField(upload_to='media')

    def __str__(self):
        return f'{self.user} | {self.title} | {self.description} | {self.date_published}'


class Comment(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='comments')
    play = models.ForeignKey(
        Play, on_delete=models.CASCADE, related_name='plays')
    created_comment = models.DateField(auto_now=True)
    updated_comment = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.user} | {self.content} | {self.created_comment} | {self.updated_comment}'


class Rating(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='user_rating')
    play = models.ForeignKey(
        Play, on_delete=models.CASCADE, related_name='plays_rating')
    rating = models.PositiveBigIntegerField(
        default=0, choices=IMPORTANCE_CHOICE)

    def __str__(self):
        return f'{self.user} | {self.play} | {self.rating}'


class Profile(models.Model):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, related_name='profiles')
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user} | {self.description}'
