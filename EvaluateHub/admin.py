from django.contrib import admin
from EvaluateHub.models import *

@admin.register(EvaluationForm)
class EvaluationFormAdmin(admin.ModelAdmin):
    pass
@admin.register(StudentsAffairs)
class StudentsAffairsAdmin(admin.ModelAdmin):
    pass
@admin.register(WorkersAffairs)
class WorkersAffairsAdmin(admin.ModelAdmin):
    pass