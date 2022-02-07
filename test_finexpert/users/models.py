from django.db import models
from data_source.dataSource import DataSource
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager, DataSource):
    def create_user(self, first_name, last_name, email):
        user = self.model(first_name=first_name, 
                          last_name=last_name, email=email)
        user.save()
        return user

    # To query : MyUser.objects.query(**kwargs).using(db)
    def query(self, **kwargs):
        return self.filter(**kwargs)

    def name(self):
        return self

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email