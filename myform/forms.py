from django import forms

# class ChildClass(module.ParentClass):

class InputForm(forms.Form):
    #1. Properties
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    roll_no = forms.IntegerField(help_text="Please enter number only") # 1--->
    password = forms.CharField(widget=forms.PasswordInput())
    
    #constructor
    
    #methods
    
    #Nested Class
    pass
