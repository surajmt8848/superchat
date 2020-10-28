from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_img.png"}'


def get_default_profile_image():
    return "image/super.jpg"


class Account():
    email = models.EmailField(
        max_length=255, unique=True, verbose_name="email")
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,
                                      null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def get_profile_image_file_name(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/{self.pk}/'):]
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    

