from django.shortcuts import render,redirect
from app.forms import SignupForm,ForgetpassForm
from app.models import Signupmodel

# Create your views here.


def indexview(request):
    return render(request, "index.html")


def signup(request):
    print(request.POST)
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
           return render(request,"signup.html")       
    return render(request,"signup.html")


def login(request):
    if request.method=="POST":
        print(request.POST)
        if Signupmodel.objects.filter(email=request.POST['logemail']).exists():
            sig=Signupmodel.objects.get(email=request.POST['logemail'])
            if sig.password==request.POST['logpass']:
                return redirect('index')
    return render(request,'login.html')




def forgotpassword(request):
    if request.method == "POST":
        print(request.POST)
        if Signupmodel.objects.filter(email=request.POST['email']).exists:
            data=Signupmodel.objects.get(email=request.POST['email'])
            return redirect(f'/passwordupdate/{data.id}')

    return render(request,"forgotpassword.html")


def passwordupdate(request,id):
    data=Signupmodel.objects.get(id=id)
    if request.method =="POST":
        form=ForgetpassForm(request.POST,instance=data)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=ForgetpassForm(instance=data)
    return render(request,"passwordupdate.html",{"data":data,"form":form})


def songpage1(request):
    return render(request,'demo.html')