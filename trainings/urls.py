from django.urls import path
from trainings import views

app_name = 'trainings'

urlpatterns = [
    path('exercises/', views.ExerciseView.as_view(), name='exercise_list'),
]