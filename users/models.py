from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyAccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, gender, image=None, password=None, ):
        # Creates and save a new user

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            image=image,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, gender, image=None, password=None):
        # Creates and save a new superUser

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            image=image,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    male = 'M'
    female = 'F'
    GENDER_CHOICES = [(male, 'Male'), (female, 'Female')]

    username = None
    email = models.EmailField(verbose_name='email', max_length=255, unique=True, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    image = models.ImageField(default='default.jpg', upload_to='upload/', null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} Profile'
