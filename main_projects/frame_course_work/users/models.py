from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from datetime import datetime


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance, 'picture.' + filename.split('.')[-1])


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(verbose_name='Image', upload_to=user_directory_path, null=True, blank=True)
    # rooms = models.ForeignKey(to=Room, on_delete=models.PROTECT, related_name='+', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('userprofile', kwargs={'user_id': self.pk})

    def __str__(self):
        return self.username


class Room(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user1_id = models.BigIntegerField(verbose_name='ID1')
    user2_id = models.BigIntegerField(verbose_name='ID2')

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.BigIntegerField(verbose_name ='room_id')
