from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Cars(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    text = models.TextField()
    image = models.ImageField(upload_to='posts/')



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()