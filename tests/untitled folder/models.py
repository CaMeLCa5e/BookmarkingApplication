from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.http import urlquote

# Create your models here.

class BookmarkUserManager(UserManager):
    def create_user(self, username, internal_id, password=None):
        user = self.model(
            username=username,
            internal_id=internal_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, internal_id, password):
        user = self.create_user(username, internal_id, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user



class BookmarkUser(AbstractUser):
    internal_id = models.CharField(max_length=25, null=True, blank=True, unique=True)
    verified = models.BooleanField(null=False, blank=True, default=False)
    approval_date = models.DateTimeField(null=True, blank=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['internal_id',]
    
    objects = BookmarkUserManager()

    def get_full_name(self):
        return self.internal_id

    def get_short_name(self):
        return self.internal_id

    def get_absolute_url(self):
        return "/u/" % urlquote(self.internal_id)

    def __str__(self):
        return self.internal_id
