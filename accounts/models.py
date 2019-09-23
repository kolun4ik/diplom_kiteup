from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/', blank=True)

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)
