from django.db import models


class Teacher(models.Model):
    firstname = models.CharFiel(max_length=50)
    lastname = models.CharFiel(max_length=50)
    work = models.CharFiel(max_length=50)
    years = models.IntergerFiel(null=True)

def __str__(self):
    return f"{self.firstname} {self.lastname}"