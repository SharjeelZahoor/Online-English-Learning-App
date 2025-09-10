from django.urls import path
from . import views

app_name = 'learning'

urlpatterns = [
    # ---------------- COURSES ----------------
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:pk>/edit/', views.edit_course, name='course_edit'),
    path('courses/<int:pk>/delete/', views.delete_course, name='course_delete'),

   # ---------------- LESSONS ----------------
    path("<int:course_id>/lessons/", views.lesson_list, name="lesson_list"),
    path("<int:course_id>/lessons/create/", views.lesson_create, name="lesson_create"),
    path("<int:course_id>/lessons/<int:lesson_id>/edit/", views.lesson_edit, name="lesson_edit"),
    path("<int:course_id>/lessons/<int:lesson_id>/delete/", views.lesson_delete, name="lesson_delete"),
    
    
  # ---------------- EXERCISES ----------------
    path("lessons/<int:lesson_id>/exercises/", views.exercise_list, name="exercise_list"),
    path("lessons/<int:lesson_id>/exercises/create/", views.exercise_create, name="exercise_create"),
    path("lessons/<int:lesson_id>/exercises/<int:exercise_id>/", views.exercise_detail, name="exercise_detail"),
    path("lessons/<int:lesson_id>/exercises/<int:exercise_id>/edit/", views.exercise_edit, name="exercise_edit"),
    path("lessons/<int:lesson_id>/exercises/<int:exercise_id>/delete/", views.exercise_delete, name="exercise_delete"),

]
