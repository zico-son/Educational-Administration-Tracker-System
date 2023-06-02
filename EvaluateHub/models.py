from django.db import models
from django.conf import settings
from EvaluateHub.translations import *

class ClassRecord(models.Model):
    choices = [
        ('primary', 'primary'),
        ('intermediate', 'intermediate'),
        ('secondary', 'secondary'),
    ]
    registered = models.IntegerField(null=True, blank=True)
    present = models.IntegerField(null=True, blank=True)
    absent = models.IntegerField(null=True, blank=True)
    level = models.CharField(max_length=12, null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.registered is None and self.present is None:
            self.absent = None
        else:
            self.absent = self.registered - self.present
        super(ClassRecord, self).save(*args, **kwargs)

class StudentsAffairs(models.Model):
    choices =[
        (disciplined, 1),
        (undisciplined, 0),
    ]
    first_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="first_class", null=True)
    second_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="second_class", null=True)
    third_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="third_class", null=True)
    fourth_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="fourth_class", null=True)
    fifth_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="fifth_class", null=True)
    sixth_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="sixth_class", null=True)
    transfers_to_school = models.IntegerField(null=True, blank=True)
    transfers_from_school = models.IntegerField(null=True, blank=True)
    transferred_files = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class SecurityFactors(models.Model):
    choices =[
        (valid, 1),
        (invalid, 0),
    ]
    fire_line = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    tanks = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    buckets = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    fire_extinguishers = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class SecuritySafety(models.Model):
    choices =[
        (disciplined, 1),
        (undisciplined, 0),
    ]
    labs = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    cabins = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    building = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    wall = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    external_factors = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    security_factors = models.OneToOneField(SecurityFactors, on_delete=models.CASCADE, related_name="security_factors")


class Material (models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    increase = models.IntegerField(null=True, blank=True)
    decrease = models.IntegerField(null=True, blank=True)
class Teachers(models.Model):
    material_one = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True)
    material_two = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_two")
    material_three = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_three")
    material_four = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_four")
    material_five = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_five")
    material_six = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_six")
    material_seven = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_seven")
    material_eight = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_eight")
    material_nine = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_nine")
    material_ten = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_ten")
    material_eleven = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_eleven")
    material_twelve = models.OneToOneField(Material, on_delete=models.CASCADE, null=True, blank=True, related_name="material_twelve")

class StrategicPlanning(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    obstacles = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    plan_activation = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    team_building = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    plan = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    analysis = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class Administration(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    execution_plan = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    team_building = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    analysis = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    activities_activation = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    obstacles = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    predicted_crisis = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    communication_system = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    risks_indicators = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    plan = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    training_on_plan = models.CharField(max_length=11, null=True, blank=True, choices=choices)
class Quality(models.Model):
    first_year_one = models.IntegerField(null=True, blank=True)
    second_year_one = models.IntegerField(null=True, blank=True)
    third_year_one = models.IntegerField(null=True, blank=True)
    fourth_year_one = models.IntegerField(null=True, blank=True)
    fifth_year_one = models.IntegerField(null=True, blank=True)
    sixth_year_one = models.IntegerField(null=True, blank=True)

    first_year_two = models.IntegerField(null=True, blank=True)
    second_year_two = models.IntegerField(null=True, blank=True)
    third_year_two = models.IntegerField(null=True, blank=True)
    fourth_year_two = models.IntegerField(null=True, blank=True)
    fifth_year_two = models.IntegerField(null=True, blank=True)
    sixth_year_two = models.IntegerField(null=True, blank=True)

    first_year_three = models.IntegerField(null=True, blank=True)
    second_year_three = models.IntegerField(null=True, blank=True)
    third_year_three = models.IntegerField(null=True, blank=True)
    fourth_year_three = models.IntegerField(null=True, blank=True)
    fifth_year_three = models.IntegerField(null=True, blank=True)
    sixth_year_three = models.IntegerField(null=True, blank=True)

class WorkersAffairs(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    registered = models.IntegerField(null=True, blank=True)
    present = models.IntegerField(null=True, blank=True)
    absent = models.IntegerField(null=True, blank=True)
    negatives =models.CharField(max_length=11, null=True, blank=True, choices=choices)
    percentage_of_absence = models.IntegerField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.absent = self.registered - self.present
        self.percentage_of_absence = (self.absent / self.registered) * 100
        super(WorkersAffairs, self).save(*args, **kwargs)


class Training(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    teachers_training = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    training_plan = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    training_plan_activation = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class Nutrition(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    daily_received = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    daily_served = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    disciplined_distribution = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    health_certificate = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    not_stored_periods = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class Decentralization(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    board_of_trustees = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    decentralization_committee = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    settlement = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    exchange = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    plan = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    append = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class Cooperative(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    existing_authorized_items = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    drag_running = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    drag_profits = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class Laboratories(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    work_validity = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    ory_association = models.IntegerField(null=True, blank=True)
    networks =models.IntegerField(null=True, blank=True)
    computers = models.IntegerField(null=True, blank=True)
    evaluation = models.IntegerField(null=True, blank=True)
    tilo = models.IntegerField(null=True, blank=True)


class ProductionUnit(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    profit_distribution = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    supply = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    activation = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    certified = models.CharField(max_length=11, null=True, blank=True, choices=choices)


class EnvironmentPopulation(models.Model):
    choices =[
        (exits, 1),
        (noexist, 0),
    ]
    toilets_health_procedures = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    health_file = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    diagnosis_health_plan = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    check_health_plan= models.CharField(max_length=11, null=True, blank=True, choices=choices)
    activities = models.CharField(max_length=11, null=True, blank=True, choices=choices)
    labs_health_procedures = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class EvaluationForm(models.Model):
    school_id = models.CharField(max_length=200, null=True, blank=True)
    school_name = models.CharField(max_length=200, null=True, blank=True)
    school_level = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by") # Tracker
    students_affairs = models.OneToOneField(StudentsAffairs, on_delete=models.CASCADE)
    workers_affairs = models.OneToOneField(WorkersAffairs, on_delete=models.CASCADE)
    strategic_planning = models.OneToOneField(StrategicPlanning, on_delete=models.CASCADE)
    production_unit = models.OneToOneField(ProductionUnit, on_delete=models.CASCADE)
    decentralization = models.OneToOneField(Decentralization, on_delete=models.CASCADE)
    environment_population = models.OneToOneField(EnvironmentPopulation, on_delete=models.CASCADE)
    administration = models.OneToOneField(Administration, on_delete=models.CASCADE)
    cooperative = models.OneToOneField(Cooperative, on_delete=models.CASCADE)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE)
    laboratories = models.OneToOneField(Laboratories, on_delete=models.CASCADE)
    training = models.OneToOneField(Training, on_delete=models.CASCADE)
    quality = models.OneToOneField(Quality, on_delete=models.CASCADE)
    security_safety = models.OneToOneField(SecuritySafety, on_delete=models.CASCADE)
    teachers = models.OneToOneField(Teachers, on_delete=models.CASCADE)
    
    


    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ["-created_at"]

class SchoolInfo(models.Model):
    total_schools = models.IntegerField(null=True, blank=True)
    last_school_added = models.CharField(max_length=255, null=True, blank=True)
    total_schools_primary = models.IntegerField(null=True, blank=True)
    total_schools_intermediate = models.IntegerField(null=True, blank=True)
    total_schools_secondary = models.IntegerField(null=True, blank=True)
    security_safety_issues= models.IntegerField(null=True, blank=True)
    security_safety_responses= models.IntegerField(null=True, blank=True)
    nutrition_issues = models.IntegerField(null=True, blank=True)
    nutrition_responses = models.IntegerField(null=True, blank=True)
    cooperative_issues = models.IntegerField(null=True, blank=True)
    cooperative_responses = models.IntegerField(null=True, blank=True)
    training_issues = models.IntegerField(null=True, blank=True)
    training_responses = models.IntegerField(null=True, blank=True)
    decentralization_issues = models.IntegerField(null=True, blank=True)
    decentralization_responses = models.IntegerField(null=True, blank=True)
    production_unit_issues = models.IntegerField(null=True, blank=True)
    production_unit_responses = models.IntegerField(null=True, blank=True)
    environment_population_issues = models.IntegerField(null=True, blank=True)
    environment_population_responses = models.IntegerField(null=True, blank=True)
    administration_issues = models.IntegerField(null=True, blank=True)
    administration_responses = models.IntegerField(null=True, blank=True)
    strategic_planning_issues = models.IntegerField(null=True, blank=True)
    strategic_planning_responses = models.IntegerField(null=True, blank=True)
    laboratories_issues = models.IntegerField(null=True, blank=True)
    laboratories_responses = models.IntegerField(null=True, blank=True)
    workers_affairs_issues = models.IntegerField(null=True, blank=True)
    workers_affairs_responses = models.IntegerField(null=True, blank=True)
    students_affairs_issues = models.IntegerField(null=True, blank=True)
    students_affairs_responses = models.IntegerField(null=True, blank=True)
    quality_issues = models.IntegerField(null=True, blank=True)
    quality_responses = models.IntegerField(null=True, blank=True)
    teachers_issues = models.IntegerField(null=True, blank=True)
    teachers_responses = models.IntegerField(null=True, blank=True)


# Issues Models
class StudentAffairsIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(StudentsAffairs, on_delete=models.CASCADE, related_name='issue')

class WorkersAffairsIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(WorkersAffairs, on_delete=models.CASCADE, related_name='issue')

class AdministrationIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Administration, on_delete=models.CASCADE, related_name='issue')

class EnvironmentPopulationIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(EnvironmentPopulation, on_delete=models.CASCADE, related_name='issue')

class StrategicPlanningIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(StrategicPlanning, on_delete=models.CASCADE, related_name='issue')

class ProductionUnitIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(ProductionUnit, on_delete=models.CASCADE, related_name='issue')

class DecentralizationIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Decentralization, on_delete=models.CASCADE, related_name='issue')

class LaboratoriesIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Laboratories, on_delete=models.CASCADE, related_name='issue')

class SecuritySafetyIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(SecuritySafety, on_delete=models.CASCADE, related_name='issue')

class NutritionIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Nutrition, on_delete=models.CASCADE, related_name='issue')

class CooperativeIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Cooperative, on_delete=models.CASCADE, related_name='issue')

class TrainingIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Training, on_delete=models.CASCADE, related_name='issue')

class QualityIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Quality, on_delete=models.CASCADE, related_name='issue')

class TeachersIssue(models.Model):
    issue = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Teachers, on_delete=models.CASCADE, related_name='issue')


# Response Models
class StudentAffairsResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(StudentsAffairs, on_delete=models.CASCADE, related_name='response')

class WorkersAffairsResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(WorkersAffairs, on_delete=models.CASCADE, related_name='response')

class AdministrationResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Administration, on_delete=models.CASCADE, related_name='response')

class EnvironmentPopulationResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(EnvironmentPopulation, on_delete=models.CASCADE, related_name='response')

class StrategicPlanningResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(StrategicPlanning, on_delete=models.CASCADE, related_name='response')

class ProductionUnitResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(ProductionUnit, on_delete=models.CASCADE, related_name='response')

class DecentralizationResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Decentralization, on_delete=models.CASCADE, related_name='response')

class LaboratoriesResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Laboratories, on_delete=models.CASCADE, related_name='response')

class SecuritySafetyResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(SecuritySafety, on_delete=models.CASCADE, related_name='response')

class NutritionResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Nutrition, on_delete=models.CASCADE, related_name='response')

class CooperativeResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Cooperative, on_delete=models.CASCADE, related_name='response')

class TrainingResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Training, on_delete=models.CASCADE, related_name='response')

class QualityResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Quality, on_delete=models.CASCADE, related_name='response')

class TeachersResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    department = models.OneToOneField(Teachers, on_delete=models.CASCADE, related_name='response')
