from django.db import models
from django.utils.timezone import now


class Member(models.Model):
    first_name = models.CharField(null = False, default = "friend", blank = False, max_length = 30)
    last_name = models.CharField(null = True, max_length = 30)
    assignement = models.CharField(null = True, max_length = 30)
    assignement_description = models.CharField(null = True, max_length = 255)
    

class Task(models.Model):
    SUBJECT_CHOICES = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Linux', 'Linux'),
        ('Networking', 'Networking'),
        ('C_Programming', 'C_Programming'),
        ('Algorythms', 'Algorythms'),
        ('Optimization', 'Optimization'),
        ('Cryptography', 'Cryptography'),
        ('Computer_Architecture', 'Computer_Architecture'),
        ('Data_Structures', 'Data_Structures'),
    ]
    LOCATION_CHOICES = [
        ('Home', 'Home'),
        ('Other', 'Other'),
        ('University', 'University'),
    ]
    title = models.CharField(max_length = 30, null = False, blank = True, default = "task")
    description = models.TextField(max_length = 255, null = True, blank = True, default = title)
    start_time = models.DateTimeField(null = False, default = now)
    end_time = models.DateTimeField(null = True, blank = True)
    time_left = models.DateTimeField(null = True, blank= True)
    location = models.CharField(null = True, max_length = 40, choices = LOCATION_CHOICES, default = 'H')
    subject = models.CharField(null = True, max_length = 30, choices = SUBJECT_CHOICES, default = 'Py')
    members = models.ForeignKey(to = Member, on_delete=models.CASCADE, null = True, blank = True)


class Custom_User(models.Model):
    username = models.CharField(null = False, max_length = 50, unique = True, default = "User")
    password = models.CharField(null = True, max_length = 100, editable = False)
    salt = models.CharField(null = True, max_length = 50, editable = False)
    tasks = models.ManyToManyField(to = Task, related_name= "users", null = True)
