from django.db import models

# Create your models here.

class StudentModel(models.Model):
    #properyies
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True);
    updates_at = models.DateTimeField(auto_now=True);
    
    #constructor
    
    #methods
    def __str__(self):
        return self.name +" "+ str(self.age)
        pass
    
    #Nested Class
    class Meta():
        db_table = "myform_studentmodel"
        pass
    pass