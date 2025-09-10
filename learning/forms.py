from django import forms
from .models import Course, Lesson, Exercise

# ---------------- COURSES ----------------
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'skill_level', 'category']

# ---------------- LESSONS ----------------


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [
            "title",
            "content",
            "video_url",
            "audio_url",
            "image",
            "flashcards",
            "order",
        ]

# ---------------- EXERCISES ----------------
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_type', 'question', 'options', 'answer']
