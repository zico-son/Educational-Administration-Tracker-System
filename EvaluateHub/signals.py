from django.db.models.signals import post_save
from django.dispatch import receiver
from EvaluateHub.models import *

@receiver(post_save, sender=EvaluationForm)
def update_school_info(sender, instance, **kwargs):
    if kwargs['created']:
        school_count = EvaluationForm.objects.count()
        last_school = EvaluationForm.objects.latest('created_at')
        (school_info, created)= SchoolInfo.objects.get_or_create(pk=1)
        school_info.total_schools = school_count
        school_info.last_school_added = last_school.school_name
        school_info.security_safety_issues = SecuritySafetyIssue.objects.count()
        school_info.security_safety_responses = SecuritySafetyResponse.objects.count()
        school_info.nutrition_issues = NutritionIssue.objects.count()
        school_info.nutrition_responses = NutritionResponse.objects.count()
        school_info.administration_issues = AdministrationIssue.objects.count()
        school_info.administration_responses = AdministrationResponse.objects.count()
        school_info.cooperative_issues = CooperativeIssue.objects.count()
        school_info.cooperative_responses = CooperativeResponse.objects.count()
        school_info.training_issues = TrainingIssue.objects.count()
        school_info.training_responses = TrainingResponse.objects.count()
        school_info.decentralization_issues = DecentralizationIssue.objects.count()
        school_info.decentralization_responses = DecentralizationResponse.objects.count()
        school_info.production_unit_issues = ProductionUnitIssue.objects.count()
        school_info.production_unit_responses = ProductionUnitResponse.objects.count()
        school_info.environment_population_issues = EnvironmentPopulationIssue.objects.count()
        school_info.environment_population_responses = EnvironmentPopulationResponse.objects.count()
        school_info.strategic_planning_issues = StrategicPlanningIssue.objects.count()
        school_info.strategic_planning_responses = StrategicPlanningResponse.objects.count()
        school_info.laboratories_issues = LaboratoriesIssue.objects.count()
        school_info.laboratories_responses = LaboratoriesResponse.objects.count()
        school_info.workers_affairs_issues = WorkersAffairsIssue.objects.count()
        school_info.workers_affairs_responses = WorkersAffairsResponse.objects.count()
        school_info.students_affairs_issues = StudentAffairsIssue.objects.count()
        school_info.students_affairs_responses = StudentAffairsResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=SecuritySafetyResponse)
def update_security_safety_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.security_safety_responses = SecuritySafetyResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=CooperativeResponse)
def update_cooperative_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.cooperative_responses = CooperativeResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=NutritionResponse)
def update_nutrition_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.nutrition_responses = NutritionResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=AdministrationResponse)
def update_administration_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.administration_responses = AdministrationResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=TrainingResponse)
def update_training_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.training_responses = TrainingResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=DecentralizationResponse)
def update_decentralization_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.decentralization_responses = DecentralizationResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=ProductionUnitResponse)
def update_production_unit_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.production_unit_responses = ProductionUnitResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=EnvironmentPopulationResponse)
def update_environment_population_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.environment_population_responses = EnvironmentPopulationResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=StrategicPlanningResponse)
def update_strategic_planning_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.strategic_planning_responses = StrategicPlanningResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=LaboratoriesResponse)
def update_laboratories_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.laboratories_responses = LaboratoriesResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=WorkersAffairsResponse)
def update_workers_affairs_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.workers_affairs_responses = WorkersAffairsResponse.objects.count()
        school_info.save()

@receiver(post_save, sender=StudentAffairsResponse)
def update_student_affairs_responses(sender, instance, **kwargs):
    if kwargs['created']:
        school_info = SchoolInfo.objects.get(pk=1)
        school_info.students_affairs_responses = StudentAffairsResponse.objects.count()
        school_info.save()