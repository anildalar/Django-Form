from django.shortcuts import render

from myform.forms import InputForm

# Create your views here.


def myView(request):
    print('Hello')
    context = {}
    # Creating an object form the class
    # object = ClassName();
    context['anil'] = InputForm()
    # Every function return something
    return render(request,'index.html',context);
