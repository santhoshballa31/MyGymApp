from django.contrib import messages
from datetime import date
from .models import Exercise, WorkoutDay, WorkoutSplit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegisterForm  
from .forms import EmailLoginForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # saves the user with a hashed password
            raw_password = form.cleaned_data.get('password1')  # UserCreationForm field

            # Try username-first (ModelBackend), then email (EmailBackend)
            auth_user = authenticate(request, username=user.username, password=raw_password)
            if auth_user is None:
                # If your EmailBackend expects the email in `username`, use username=user.email instead.
                # If it expects `email=...`, keep email=...
                auth_user = authenticate(request, email=user.email, password=raw_password)

            if auth_user is not None:
                login(request, auth_user)
                messages.success(request, f"Welcome {auth_user.username}, your account has been created!")
                return redirect('dashboard')
            else:
                messages.error(request, "Authentication failed right after registration. Check backends/signature.")
    else:
        form = RegisterForm()
    return render(request, 'overload_tracker/register.html', {'form': form})


class CustomLoginView(View):
    def get(self, request):
        form = EmailLoginForm()
        return render(request, 'overload_tracker/login.html', {'form': form})

    def post(self, request):
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'overload_tracker/login.html', {'form': form})


@login_required 
def dashboard(request):
    current_user = request.user
    current_date = date.today()

    # Try to find the active split (safe version)
    active_split = WorkoutSplit.objects.filter(is_active=True).first()

    template_splits = WorkoutSplit.objects.filter(is_custom = False)
    
    if active_split:
        days = active_split.days.all().order_by('order')
    else:
        days = []

    # (We’ll render this to a template next)
    print(f"User: {current_user.username}")
    print(f"Date: {current_date}")
    print(f"Active split: {active_split}")
    print(f"Days: {days}")

    return render(request, "overload_tracker/dashboard.html", {
        "user": current_user,
        "date": current_date,
        "active_split": active_split,
        "days": days,
        "template_splits": template_splits, 
    })


#this will be a button that will show up in dashboard 
#create def view for dropdown
from django.shortcuts import get_object_or_404

@login_required
def select_split_from_dropdown(request):
    if request.method == "POST":
        split_id = request.POST.get("split_id")
        template_split = get_object_or_404(WorkoutSplit, id=split_id, is_custom=False)

        # Clone split for user
        user_split = WorkoutSplit.objects.create(
            name=template_split.name,
            is_custom=True,
            is_active=True
        )

        for day in template_split.days.all():
            new_day = WorkoutDay.objects.create(
                name=day.name,
                split=user_split,
                order=day.order
            )
            for ex in day.exercises.all():
                Exercise.objects.create(
                    name=ex.name,
                    workout_day=new_day,
                    order=ex.order
                )

        # Deactivate other splits
        WorkoutSplit.objects.filter(is_custom=True).exclude(id=user_split.id).update(is_active=False)

        return redirect('dashboard')

    return redirect('dashboard')
