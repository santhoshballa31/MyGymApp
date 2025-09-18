import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gym_project.settings")
django.setup()

from overload_tracker.models import WorkoutSplit, WorkoutDay, Exercise

if WorkoutSplit.objects.filter(name='Full Body', is_custom=False).exists():
    print("Full Body Split already exists. Skipping.")
else:
    fullbody_split = WorkoutSplit.objects.create(name='Full Body', is_custom=False)

    fullbody_A = WorkoutDay.objects.create(name='Full Body Day A', split=fullbody_split, order=1)
    fullbody_B = WorkoutDay.objects.create(name='Full Body Day B', split=fullbody_split, order=2)
    fullbody_C = WorkoutDay.objects.create(name='Full Body Day C', split=fullbody_split, order=3)

    Exercise.objects.create(name="Chest Press", workout_day=fullbody_A, order=1)
    Exercise.objects.create(name="Lat Pulldown", workout_day=fullbody_A, order=2)
    Exercise.objects.create(name="Shoulder Press", workout_day=fullbody_A, order=3)
    Exercise.objects.create(name="Bicep Curl", workout_day=fullbody_A, order=4)
    Exercise.objects.create(name="Tricep Pushdown", workout_day=fullbody_A, order=5)
    Exercise.objects.create(name="Squat Pattern", workout_day=fullbody_A, order=6)
    Exercise.objects.create(name="RDL", workout_day=fullbody_A, order=7)

    Exercise.objects.create(name="Incline Chest Press", workout_day=fullbody_B, order=1)
    Exercise.objects.create(name="Wide Grip Row", workout_day=fullbody_B, order=2)
    Exercise.objects.create(name="Lateral Raise", workout_day=fullbody_B, order=3)
    Exercise.objects.create(name="Bicep Curl", workout_day=fullbody_B, order=4)
    Exercise.objects.create(name="Tricep Pushdown", workout_day=fullbody_B, order=5)
    Exercise.objects.create(name="Leg Extension", workout_day=fullbody_B, order=6)
    Exercise.objects.create(name="Hamstring Curl", workout_day=fullbody_B, order=7)

    Exercise.objects.create(name="Chest Fly", workout_day=fullbody_C, order=1)
    Exercise.objects.create(name="Trap-Focused Shrugs", workout_day=fullbody_C, order=2)
    Exercise.objects.create(name="Rear Delt Fly", workout_day=fullbody_C, order=3)
    Exercise.objects.create(name="Bicep Curl", workout_day=fullbody_C, order=4)
    Exercise.objects.create(name="Tricep Pushdown", workout_day=fullbody_C, order=5)
    Exercise.objects.create(name="Calf Raise", workout_day=fullbody_C, order=6)
    Exercise.objects.create(name="Adductor Machine", workout_day=fullbody_C, order=7)

    print("✅ Full Body Split seeded successfully.")
