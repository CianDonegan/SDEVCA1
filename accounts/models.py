from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

# don think this user model is suitable for our purposes another one we have ourself called user i believe would also be a good option

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null = True, on_delete=models.CASCADE,)
    date_of_birth = models.DateField(blank=False, null=False)
    fav_author = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)
