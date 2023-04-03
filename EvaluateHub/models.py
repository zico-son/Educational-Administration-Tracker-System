from django.db import models
from django.conf import settings
# Models for the EvaluateHub app
# Models are the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
class Tracker (models.Model):
    # Tracker is a model that represents a tracker that can be used to track the progress of a product.
    # The tracker is made up of a series of steps that are completed by the user. The steps are then used to calculate a score for the product.
    # The Tracker model contains the following fields:
    # name: The name of the tracker.
    # description: A description of the tracker.
    # steps: A list of steps that are asked on the tracker.
    # 
    # Fields
    # name
    # description
    # steps
    #
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    steps = models.TextField(null=True, blank=True)
    # Methods
    # __str__() - Returns the name of the tracker.
    def str(self):
        return self.name
    
class EvaluationForm (models.Model):
    # EvaluationForm is a model that represents a form that can be filled out by a user to evaluate a school.
    # The form is made up of a series of questions that are answered by the user. The answers are then used to calculate a score for the product.
    # The EvaluationForm model contains the following fields:
    # school_name: The name of the school.
    # school_id: The id of the school.
    # school_address: The address of the school.
    # department_one_review: A review of the first department. as like as department_two_review, department_three_review, department_four_review, department_five_review, department_six_review, department_seven_review, department_eight_review, department_nine_review.
    # created_at: The date and time that the form was created.
    # updated_at: The date and time that the form was last updated.
    # created_by: The user that created the form.
    # status: The status of the form.
    school_name = models.CharField(max_length=255, null=True, blank=True)
    school_id = models.CharField(max_length=255, null=True, blank=True)
    school_address = models.CharField(max_length=255, null=True, blank=True)
    department_one_review = models.TextField(null=True, blank=True)
    department_two_review= models.TextField(null=True, blank=True)
    department_three_review = models.TextField(null=True, blank=True)
    department_four_review = models.TextField(null=True, blank=True)
    department_five_review = models.TextField(null=True, blank=True)
    department_six_review = models.TextField(null=True, blank=True)
    department_seven_review = models.TextField(null=True, blank=True)
    department_eight_review = models.TextField(null=True, blank=True)
    department_nine_review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Tracker, on_delete=models.PROTECT)
    notes = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

