import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gym_project.settings")
django.setup()

from overload_tracker.models import WorkoutSplit, WorkoutDay, Exercise


if WorkoutSplit.objects.filter(name="Upper/Lower", is_custom=False).exists():
    print("⚠️ Upper/Lower Split already exists. Skipping.")
else:
    ul_split = WorkoutSplit.objects.create(name='Upper/Lower', is_custom=False)

    upper_day = WorkoutDay.objects.create(name="Upper", split=ul_split, order=1)
    lower_day = WorkoutDay.objects.create(name="Lower", split=ul_split, order=2)

    Exercise.objects.create(name="Chest Fly", workout_day=upper_day, order=1)
    Exercise.objects.create(name="Lat Pulldown / Pull-up", workout_day=upper_day, order=2)
    Exercise.objects.create(name="Wide Grip Row", workout_day=upper_day, order=3)
    Exercise.objects.create(name="Seated Shoulder Press", workout_day=upper_day, order=4)
    Exercise.objects.create(name="Lateral Raise", workout_day=upper_day, order=5)
    Exercise.objects.create(name="Tricep Pushdowns", workout_day=upper_day, order=6)
    Exercise.objects.create(name="Bicep Curl", workout_day=upper_day, order=7)
    Exercise.objects.create(name="Tricep Dips", workout_day=upper_day, order=8)

    Exercise.objects.create(name='Squat Pattern', workout_day=lower_day, order=1)
    Exercise.objects.create(name='Leg Extension', workout_day=lower_day, order=2)
    Exercise.objects.create(name='Hamstring Curl', workout_day=lower_day, order=3)
    Exercise.objects.create(name='RDLs', workout_day=lower_day, order=4)
    Exercise.objects.create(name='Calf Raise', workout_day=lower_day, order=5)
    Exercise.objects.create(name='Adductor Machine', workout_day=lower_day, order=6)
    Exercise.objects.create(name='Abs', workout_day=lower_day, order=7)

    print("✅ Upper/Lower Split seeded successfully.")
