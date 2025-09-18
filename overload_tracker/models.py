from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#from django.contrib.auth.models import get_user_mode 

from django.core.validators import MinValueValidator, MaxValueValidator



class WorkoutSplit(models.Model):
    name = models.CharField(max_length=100)
    is_custom = models.BooleanField(default=False)
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(to = User, on_delete = models.CASCADE, related_name = 'profile')
    active_split = models.ForeignKey(WorkoutSplit, null = True, blank = True, on_delete = models.SET_NULL)


class WorkoutDay(models.Model):
    name = models.CharField(max_length = 100)
    split = models.ForeignKey(WorkoutSplit, on_delete= models.CASCADE, related_name = "days")
    order = models.PositiveIntegerField(help_text="Day number in the split (e.g. 1 = Push, 2 = Pull)")

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length = 100)
    workout_day = models.ForeignKey(WorkoutDay, on_delete = models.CASCADE, related_name = "exercises")
    order = models.PositiveIntegerField(help_text = "1st exercise of the day, 2nd exercise.... (1 = DB Press, 2 = Pec Fly")

    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")
    workout_day = models.ForeignKey(WorkoutDay, on_delete = models.CASCADE, related_name = "sessions")
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.workout_day.name} - {self.date.strftime('%B %d, %Y')}"

class ExerciseLog(models.Model):
    session = models.ForeignKey(WorkoutSession, on_delete = models.CASCADE, related_name = "exercise_logs")
    exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE, related_name = "logs")
    
    def __str__(self):
        return self.exercise.name

class SetLog(models.Model):
    reps = models.PositiveIntegerField()
    weight = models.FloatField()
    rir = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    order = models.PositiveIntegerField(help_text = "1st Set, 2nd Set(1 = 1st Set)")
    exercise_log = models.ForeignKey(ExerciseLog, on_delete = models.CASCADE, related_name = "sets" )

    def __str__(self):
        return f"{self.order} - {self.weight} x {self.reps} @ {self.rir}"
    











