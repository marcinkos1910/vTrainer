from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField()    # specific filed (like URLField) already has validation

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Exercise, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Training(models.Model):
    name = models.CharField
    exercise_1 = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='exercise_1')
    series_1 = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    repeats_1 = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    exercise_2 = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='exercise_2')
    series_2 = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    repeats_2 = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.name}'


class DailyPlan(models.Model):
    name = models.CharField(max_length=250)
    monday = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='monday_training')
    tuesday = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='tuesday_training')
    wednesday = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='wednesday_training')
    thursday = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='thursday_training')
    friday = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='friday_training')
    saturday = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='saturday_training')
    sunday = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='sunday_training')

    def __str__(self):
        return f'{self.name}'


class UserPlan(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    plan = models.ForeignKey('DailyPlan', on_delete=models.CASCADE)
    week = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(53)])

    def __str__(self):
        return f'plan:{self.plan}, user: {self.user}, week: {self.week}'
