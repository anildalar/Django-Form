from django import forms

from myform.models import StudentModel

# class ChildClass(module.ParentClass):

class InputForm(forms.ModelForm):
    #1. Properties
   
    
    #constructor
    
    #methods
    
    #Nested Class
    class Meta():
        #1. Properties
        model = StudentModel
        fields = "__all__"    
        pass
    pass
