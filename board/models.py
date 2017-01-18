from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name

class Meal(models.Model):
    school = models.ForeignKey(School)
    meal_name = models.CharField(max_length=200)
    price = models.IntegerField()
    # test


    def __str__(self):
        return self.meal_name
