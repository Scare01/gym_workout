from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

NUMBER_MONTHS_WORKOUT = (
    (4, '4 month'),
    (6, '6 month'),
    (8, '8 month'),
)


class Program(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    continuity = models.PositiveIntegerField(choices=NUMBER_MONTHS_WORKOUT)
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'


class Excercises(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rounds_count = models.PositiveIntegerField(default=0)
    max_rep = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class ExcercisesForm(ModelForm):
    class Meta:
        model = Excercises
        fields = ['name', 'rounds_count', 'max_rep']


class Rounds(models.Model):
    excercise = models.ForeignKey(Excercises, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=0)
    current_rep = models.PositiveIntegerField(default=0)


class RoundsForm(ModelForm):
    class Meta:
        model = Rounds
        fields = ['weight', 'current_rep']
