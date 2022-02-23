from django.contrib import admin

from trainings.models import Exercise, Training, DailyPlan, UserPlan

admin.site.register(Exercise)
admin.site.register(Training)
admin.site.register(DailyPlan)
admin.site.register(UserPlan)