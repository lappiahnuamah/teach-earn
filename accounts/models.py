from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import file_size


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    # user = models.OneToOneField("CustomUser", primary_key=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    comment = models.CharField(max_length=100)



class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    hostel = models.CharField(max_length=100)



class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", validators=[file_size])

    def __str__(self):
        return self.caption
    