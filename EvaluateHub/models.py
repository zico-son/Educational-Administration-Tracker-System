from django.db import models
from django.conf import settings
from EvaluateHub.translatations import disciplined, notdisciplined
class ClassRecord(models.Model):
    registered = models.IntegerField(null=True, blank=True)
    present = models.IntegerField(null=True, blank=True)
    absent = models.IntegerField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.absent = self.registered - self.present
        super(ClassRecord, self).save(*args, **kwargs)

class StudentsAffairs(models.Model):
    choices =[
        (disciplined, 1),
        (notdisciplined, 0),
    ]
    first_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="first_class")
    second_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="second_class")
    third_class = models.OneToOneField(ClassRecord, on_delete=models.CASCADE, related_name="third_class")
    transfers_to_school = models.IntegerField(null=True, blank=True)
    transfers_from_school = models.IntegerField(null=True, blank=True)
    transferred_files = models.CharField(max_length=11, null=True, blank=True, choices=choices)

class WorkersAffairs(models.Model):
    pass

class SecuritySafety(models.Model):
    pass

class Nutrition(models.Model):
    pass

class Cooperative(models.Model):
    pass

class Quality(models.Model):
    pass

class Training(models.Model):
    pass

class Laboratories(models.Model):
    pass

class Teachers(models.Model):
    pass

class Decentralization(models.Model):
    pass

class ProductionUnit(models.Model):
    pass

class StrategicPlanning(models.Model):
    pass

class EnvironmentPopulation(models.Model):
    pass

class Administration(models.Model):
    pass

class EvaluationForm(models.Model):
    school_id = models.CharField(max_length=200, null=True, blank=True)
    school_name = models.CharField(max_length=200, null=True, blank=True)
    school_type = models.CharField(max_length=200, null=True, blank=True)
    school_level = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by") # Tracker
    student_affairs = models.OneToOneField(StudentsAffairs, on_delete=models.CASCADE, related_name="student_affairs")
    workers_affairs = models.OneToOneField(WorkersAffairs, on_delete=models.CASCADE, related_name="workers_affairs")
    security_safety = models.OneToOneField(SecuritySafety, on_delete=models.CASCADE, related_name="security_safety")
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE, related_name="nutrition")
    cooperative = models.OneToOneField(Cooperative, on_delete=models.CASCADE, related_name="cooperative")
    quality = models.OneToOneField(Quality, on_delete=models.CASCADE, related_name="quality")
    training = models.OneToOneField(Training, on_delete=models.CASCADE, related_name="training")
    laboratories = models.OneToOneField(Laboratories, on_delete=models.CASCADE, related_name="laboratories")
    teachers = models.OneToOneField(Teachers, on_delete=models.CASCADE, related_name="teachers")
    decentralization = models.OneToOneField(Decentralization, on_delete=models.CASCADE, related_name="decentralization")
    production_unit = models.OneToOneField(ProductionUnit, on_delete=models.CASCADE, related_name="production_unit")
    strategic_planning = models.OneToOneField(StrategicPlanning, on_delete=models.CASCADE, related_name="strategic_planning")
    environment_population = models.OneToOneField(EnvironmentPopulation, on_delete=models.CASCADE, related_name="environment_population")
    administration = models.OneToOneField(Administration, on_delete=models.CASCADE, related_name="administration")

    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ["-created_at"]
