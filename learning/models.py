# courses/models.py
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Course(models.Model):
    SKILL_LEVELS = [
        ("BEGINNER", "Beginner"),
        ("INTERMEDIATE", "Intermediate"),
        ("ADVANCED", "Advanced"),
    ]

    CATEGORIES = [
        ("GRAMMAR", "Grammar"),
        ("VOCABULARY", "Vocabulary"),
        ("LISTENING", "Listening"),
        ("SPEAKING", "Speaking"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVELS)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content = models.TextField()

    # Multimedia options
    video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo or hosted video URL")
    audio_url = models.URLField(blank=True, null=True, help_text="Audio file or podcast URL")
    image = models.ImageField(upload_to="lesson_images/", blank=True, null=True)
    flashcards = models.JSONField(blank=True, null=True, help_text="Store flashcards as JSON [{front:'word', back:'meaning'}]")

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Exercise(models.Model):
    EXERCISE_TYPES = [
        ("QUIZ", "Quiz"),
        ("SPEAKING", "Speaking"),
        ("WRITING", "Writing"),
        ("LISTENING", "Listening"),
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="exercises")
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_TYPES)
    question = models.TextField()
    options = models.JSONField(blank=True, null=True)  # for MCQ
    answer = models.TextField()

    def __str__(self):
        return f"{self.lesson.title} - {self.exercise_type}"


class StudentProgress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'lesson', 'exercise')

    def __str__(self):
        if self.exercise:
            return f"{self.student.email} - {self.exercise.lesson.title} - {self.exercise.exercise_type}"
        return f"{self.student.email} - {self.lesson.title}"
