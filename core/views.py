from django.shortcuts import redirect, render

def home_redirect(request):
    if request.user.is_authenticated:
        # Logged-in users → redirect by role
        user = request.user
        if user.is_superuser or user.role == "ADMIN":
            return redirect("accounts:admin_dashboard")
        elif user.role == "TEACHER":
            return redirect("accounts:teacher_dashboard")
        elif user.role == "STUDENT":
            return redirect("accounts:student_dashboard")
        return redirect("accounts:login")
    else:
        # Guests → show landing page
        return render(request, "core/home.html")
