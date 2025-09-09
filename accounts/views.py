from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
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
    return render(request, "accounts/admin_dashboard.html")

@login_required
def teacher_dashboard(request):
    return render(request, "accounts/teacher_dashboard.html")

@login_required
def student_dashboard(request):
    return render(request, "accounts/student_dashboard.html")
