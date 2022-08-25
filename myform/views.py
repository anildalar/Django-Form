from django.shortcuts import render,redirect

from myform.forms import InputForm

# Create your views here.


def myView(request):
    if request.method == "POST": 
        print(request.POST) 
        form = InputForm(request.POST)  
        if form.is_valid():  
            try:
                student = form.save(commit=True)
                student.save()
                return redirect('/home')  
            except:  
                pass  
    else:  
        form = InputForm()  
        return render(request,'index.html',{'form':form}) 

