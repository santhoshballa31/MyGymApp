
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gym_project.settings")
django.setup()

from overload_tracker.models import WorkoutSplit, WorkoutDay, Exercise

ppl_split = WorkoutSplit.objects.create(name="Push/Pull/Legs", is_custom=False)

push_day = WorkoutDay.objects.create(name="Push", split=ppl_split, order=1)
pull_day = WorkoutDay.objects.create(name="Pull", split=ppl_split, order=2)
legs_day = WorkoutDay.objects.create(name="Legs", split=ppl_split, order=3)

Exercise.objects.create(name="Chest Fly", workout_day=push_day, order=1)
Exercise.objects.create(name="Seated Shoulder Press", workout_day=push_day, order=2)
Exercise.objects.create(name="Lateral Raise", workout_day=push_day, order=3)
Exercise.objects.create(name="Tricep Pushdowns", workout_day=push_day, order=4)

Exercise.objects.create(name="Lat Pulldown / Pull-up", workout_day=pull_day, order=1)
Exercise.objects.create(name="Chest-Supported Wide Row", workout_day=pull_day, order=2)
Exercise.objects.create(name="Rear Delt Exercise", workout_day=pull_day, order=3)
Exercise.objects.create(name="Bicep Curl", workout_day=pull_day, order=4)

Exercise.objects.create(name="Squat Pattern", workout_day=legs_day, order=1)
Exercise.objects.create(name="RDL / SLDL", workout_day=legs_day, order=2)
Exercise.objects.create(name="Leg Extensions", workout_day=legs_day, order=3)
Exercise.objects.create(name="Hamstring Curl", workout_day=legs_day, order=4)
Exercise.objects.create(name="Calf Raise", workout_day=legs_day, order=5)

print(" PPL Split seeded successfully.")
