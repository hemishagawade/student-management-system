from django.shortcuts import render, redirect
from stuapp.models import Student

# Create your views here.
def dashboard(request):
    # fetch data from database and display on dashboard
    data = Student.objects.all()
    context = {}
    context['students'] = data
    return render(request,'index.html',context)

def addstu(request):
    if request.method=="GET":
        return render(request,'addstu.html')
    else:
        # 1) fetch FORM data 
        n = request.POST['name'] 
        b = request.POST['branch'] 
        y = request.POST['year'] 
        d = request.POST['dob'] 
        p = request.POST['phno'] 
        e = request.POST['email'] 
        # 2) inserting data into database
        s = Student.objects.create(name=n,branch=b,year=y,dob=d,phno=p,email=e)
        s.save()
        # 3) return to dashboard
        return redirect('/dashboard')

def deletestu(request,stuid):
    s = Student.objects.filter(id=stuid)
    s.delete()
    return redirect('/dashboard')

def updatestu(request,stuid):
    if request.method=="GET":
        s = Student.objects.filter(id=stuid)
        context = {}
        context['stu'] = s[0]
        return render(request,'updatestu.html',context)
    else: 
        n = request.POST['name'] 
        b = request.POST['branch'] 
        y = request.POST['year'] 
        d = request.POST['dob'] 
        p = request.POST['phno'] 
        e = request.POST['email'] 
        s = Student.objects.filter(id=stuid)
        s.update(name=n,branch=b,year=y,dob=d,phno=p,email=e)
        return redirect('/dashboard')
    
