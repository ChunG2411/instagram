from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Prefer not to say')
]

class User(AbstractUser):
    picture = models.ImageField(upload_to = 'profile' ,null=True, blank=True)
    full_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    biography = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER ,null=True, blank=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def follower_count(self):
        count = self.followed.count()
        return count

    @property
    def following_count(self):
        count = self.follower.count()
        return count
    
    @property
    def posts_count(self):
        count = self.post_set.count()
        return count