from django.db import models
from account.models import UserAccount
# pip install django-autoslug==1.9.9
from autoslug import AutoSlugField
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=100)
    # pip install pillow
    photo = models.ImageField(upload_to='authors')
    slug = AutoSlugField(populate_from='user', unique=True, always_update=True)

    def __str__(self):
        return self.name
