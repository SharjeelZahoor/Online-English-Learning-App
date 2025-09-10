from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lesson, Exercise
from .forms import CourseForm, LessonForm, ExerciseForm
from .decorators import teacher_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson
# ---------------- COURSES ----------------

# Course list
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'learning/course_list.html', {'courses': courses})


@login_required
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('learning:course_list')
    else:
        form = CourseForm()
    return render(request, 'learning/course_form.html', {'form': form})

@teacher_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('learning:course_list')
    return render(request, 'learning/course_form.html', {'form': form})

@teacher_required
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect('learning:course_list')
    return render(request, 'learning/course_confirm_delete.html', {'course': course})

# ---------------- LESSONS ----------------
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson
from .forms import LessonForm

# List all lessons of a course
def lesson_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all().order_by("order")
    return render(request, "learning/lesson_list.html", {"course": course, "lessons": lessons})

# Create a lesson
def lesson_create(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect("lesson_list", course_id=course.id)
    else:
        form = LessonForm()
    return render(request, "learning/lesson_form.html", {"form": form, "course": course})

# Edit a lesson
def lesson_edit(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect("lesson_list", course_id=course.id)
    else:
        form = LessonForm(instance=lesson)
    return render(request, "learning/lesson_form.html", {"form": form, "course": course})

# Delete a lesson
def lesson_delete(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    if request.method == "POST":
        lesson.delete()
        return redirect("lesson_list", course_id=course.id)
    return render(request, "learning/lesson_confirm_delete.html", {"lesson": lesson, "course": course})

# ---------------- EXERCISES ----------------
@login_required
def exercise_list(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    exercises = lesson.exercise_set.all()
    return render(request, 'learning/exercise_list.html', {'lesson': lesson, 'exercises': exercises})

@teacher_required
def exercise_create(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.lesson = lesson
            exercise.save()
            return redirect('learning:exercise_list', lesson_id=lesson.id)
    else:
        form = ExerciseForm()
    return render(request, 'learning/exercise_form.html', {'form': form, 'lesson': lesson})
