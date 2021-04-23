from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from playapp.models import MyUser, Play, Comment, Rating, Profile

admin.site.register(MyUser, UserAdmin)
admin.site.register(Play)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Profile)