from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from learning.models import Course, Lesson
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=raw_password)
            if user:
                login(request, user)
                return redirect('accounts:dashboard_redirect')  # ✅ namespace added
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("accounts:dashboard_redirect")  # ✅ namespace added
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # ✅ namespace added

@login_required
def dashboard_redirect(request):
    user = request.user

    if user.is_superuser or user.role == "ADMIN":
        return redirect("accounts:admin_dashboard")
    elif user.role == "TEACHER":
        return redirect("accounts:teacher_dashboard")
    elif user.role == "STUDENT":
        return redirect("accounts:student_dashboard")
    else:
        return redirect("accounts:login")



@login_required
def admin_dashboard(request):
    courses = Course.objects.all()   # Fetch all courses
    return render(request, "accounts/admin_dashboard.html", {
        "courses": courses
    })

@login_required
def teacher_dashboard(request):
    return render(request, "accounts/teacher_dashboard.html")

@login_required
def student_dashboard(request):
    return render(request, "accounts/student_dashboard.html")


def manage_content(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    return render(request, "accounts/manage_content.html", {
        "courses": courses,
        "lessons": lessons
    })
    
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm

User = get_user_model()

# ---------------- LIST USERS ----------------
@login_required
def user_list(request):
    if not request.user.is_superuser:  # ✅ only superuser can access
        return redirect("accounts:dashboard_redirect")

    users = User.objects.all()
    return render(request, "accounts/user_list.html", {"users": users})


# ---------------- CREATE USER ----------------
@login_required
def user_create(request):
    if not request.user.is_superuser:  # ✅ only superuser can access
        return redirect("accounts:dashboard_redirect")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:user_list")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/user_form.html", {"form": form})


# ---------------- EDIT USER ----------------
@login_required
def user_edit(request, user_id):
    if not request.user.is_superuser:  # ✅ only superuser can access
        return redirect("accounts:dashboard_redirect")

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:user_list")
    else:
        form = UserUpdateForm(instance=user)

    return render(request, "accounts/user_form.html", {"form": form})


# ---------------- DELETE USER ----------------
@login_required
def user_delete(request, user_id):
    if not request.user.is_superuser:  # ✅ only superuser can access
        return redirect("accounts:dashboard_redirect")

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":  # confirm delete
        user.delete()
        return redirect("accounts:user_list")

    return render(request, "accounts/user_confirm_delete.html", {"user": user})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from learning.models import Course, Lesson, Exercise  # adjust if needed

User = get_user_model()

@login_required
def analytics_view(request):
    if not request.user.is_superuser:  # only superuser (admin)
        return redirect("accounts:dashboard_redirect")

    data = {
        "total_users": User.objects.count(),
        "total_teachers": User.objects.filter(role="TEACHER").count(),
        "total_students": User.objects.filter(role="STUDENT").count(),
        "total_courses": Course.objects.count(),
        "total_lessons": Lesson.objects.count(),
        "total_exercises": Exercise.objects.count(),
    }

    return render(request, "accounts/analytics.html", {"data": data})
