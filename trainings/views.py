from django.shortcuts import render
from django.views.generic import ListView

from trainings.models import Exercise


class ExerciseView(ListView):
    template_name = 'trainings/exercise_list.html'
    model = Exercise
    context_object_name = 'exercises'   # tbd