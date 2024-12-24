from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class UserProfileInfo(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, related_name="user_profile",on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=50)   #needed
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    teacher = 'teacher'      #needed
    student = 'student'     #needed
    department_admin = 'department_admin'
    #nihal code #needed
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (department_admin, 'department_admin'),
    ]
    user_type = models.CharField(max_length=30, choices=user_types, default=student)
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
