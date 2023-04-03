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
    

