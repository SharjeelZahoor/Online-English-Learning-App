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
    path('courses/<int:course_id>/lessons/', views.lesson_list, name='lesson_list'),
    path('courses/<int:course_id>/lessons/create/', views.lesson_create, name='lesson_create'),

    # ---------------- EXERCISES ----------------
    path('lessons/<int:lesson_id>/exercises/', views.exercise_list, name='exercise_list'),
    path('lessons/<int:lesson_id>/exercises/create/', views.exercise_create, name='exercise_create'),
]
