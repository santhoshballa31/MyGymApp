from django.contrib import admin

#Importing all our models
from .models import WorkoutSplit 
from .models import WorkoutDay 
from .models import WorkoutSession
from .models import Exercise 
from .models import ExerciseLog 
from .models import SetLog 
from .models import Profile
#Registering all our models 
admin.site.register(WorkoutSplit)
admin.site.register(WorkoutDay)
admin.site.register(WorkoutSession)
admin.site.register(Exercise)
admin.site.register(ExerciseLog)
admin.site.register(SetLog)
admin.site.register(Profile)



