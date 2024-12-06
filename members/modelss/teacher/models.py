from django.db import models


class Teacher(models.Model):
    firstname = models.CharFiel(max_lenght=50)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField()


def __str__(self):
    return f"{self.firstname}"