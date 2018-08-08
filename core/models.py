from django.db import models
from django.contrib.auth.models import User


class Program(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    continuity = models.PositiveIntegerField(default=0)
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Excercises(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rounds_count = models.PositiveIntegerField(default=0)
    max_rep = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Rounds(models.Model):
    excercise = models.ForeignKey(Excercises, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=0)
    current_rep = models.PositiveIntegerField(default=0)
