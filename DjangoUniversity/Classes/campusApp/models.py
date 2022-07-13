
from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    CampusName = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=60, default="", blank=True, null=False)
    CampusID = models.IntegerField(default="", blank=True, null=False)

    #creates model manager
    object = models.Manager()

    #displays the object output values in the form of a string
    def __str__(self):
        #returns the input value of the title and instructor name
        #field as a tuple to display in the browser instead of the default titles
        display_course = '{0.CampusName}: {0.State}'
        return display_course.format(self)

  #removes added 's' that django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campuses"