from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Education, Experience, Projects, Skills, Interests

# Create your views here.


def Login(request):
    if request.method == "POST":
        uName = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request, username=uName, password=passwd)
        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'login.html')

def Signup(request):
    if request.method == "POST":
        fName = request.POST['fname']
        lName = request.POST['lname']
        uName = request.POST['username']
        eMail = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']
        if pass1==pass2:
            user = User.objects.create_user(first_name=fName, last_name=lName, username=uName, email=eMail, password=pass1)
            user.save()
        else:
            messages.error(request, 'Passwords does not match!')
        

    return render(request, 'signup.html')

def index(request):
    if User:
        logout(request)
    return render(request, 'index.html')

@login_required(login_url='/login')
def dashboard(request):
    
    us = request.user
    prof = Profile.objects.filter(user = us)

    context = {
        'prof':prof,
    }
    return render(request, 'dashboard.html', context)



def Logout(request):
    logout(request)
    return redirect(Login)



def CreateResume(request, id):
    if request.method == 'POST':
        FName = request.POST['firstName']
        LName = request.POST['lastName']
        Gender = request.POST['gender']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Address = request.POST['address']
        Role = request.POST['role']
        Desc = request.POST['desc']

        Degree1 = request.POST['degree1']
        College1 = request.POST['college1']
        Gpa1 = request.POST['gpa1']
        Degree2 = request.POST['degree2']
        College2 = request.POST['college2']
        Gpa2 = request.POST['gpa2']

        CompName1 = request.POST['CompName1']
        CompPeriod1 = request.POST['CompPeriod1']
        CompRole1 = request.POST['CompRole1']
        CompName2 = request.POST['CompName2']
        CompPeriod2 = request.POST['CompPeriod2']
        CompRole2 = request.POST['CompRole2']

        Proj1 = request.POST['Proj1']
        ProjDesc1 = request.POST['ProjDesc1']
        Proj2 = request.POST['Proj2']
        ProjDesc2 = request.POST['ProjDesc2']

        skills = request.POST['skills']

        interest = request.POST['interest']

        if FName != '':
            data = Profile.objects.create(user_id=id,fname=FName, lname=LName, gender=Gender, email=Email, phone=Phone, address=Address, role=Role, desc=Desc)
            ed = Education.objects.create(profile_id=data.id,degree1=Degree1, college1=College1, gpa1=Gpa1,degree2=Degree2, college2=College2, gpa2=Gpa2)
            exp = Experience.objects.create(profile_id=data.id, compName1=CompName1,compPeriod1=CompPeriod1,compRole1=CompRole1,compName2=CompName2,compPeriod2=CompPeriod2,compRole2=CompRole2)
            proj = Projects.objects.create(profile_id=data.id,proj1=Proj1,projDesc1=ProjDesc1,proj2=Proj2,projDesc2=ProjDesc2)
            skls = Skills.objects.create(profile_id=data.id,skills=skills)
            ints = Interests.objects.create(profile_id=data.id, interests=interest)
        else:
            return render(request, 'createResume.html')


        data.save()
        ed.save()
        exp.save()
        proj.save()
        skls.save()
        ints.save()

        return redirect(dashboard)
    else:
        return render(request, 'createResume.html')
    



def ViewResume(request, id):
    prof = Profile.objects.get(id = id)
    ed = Education.objects.get(profile_id=id)
    exp = Experience.objects.get(profile_id=id)
    proj = Projects.objects.get(profile_id=id)
    skills = Skills.objects.get(profile_id=id)
    interests = Interests.objects.get(profile_id=id)

    
    context ={
        'profile' : prof,
        'ed' : ed,
        'exp':exp,
        'proj':proj,
        'skls':skills,
        'ints':interests,
    }
    return render(request, 'viewresume.html', context)


def updateResume(request, id):
    prof = Profile.objects.get(id = id)
    ed = Education.objects.get(profile_id=id)
    exp = Experience.objects.get(profile_id=id)
    proj = Projects.objects.get(profile_id=id)
    skills = Skills.objects.get(profile_id=id)
    interests = Interests.objects.get(profile_id=id)

    context ={
        'prof' : prof,
        'ed' : ed,
        'exp':exp,
        'proj':proj,
        'skls':skills,
        'ints':interests,
    }
    if request.method=='POST':
        prof.fname = request.POST['firstName']
        prof.lname = request.POST['lastName']
        prof.gender = request.POST['gender']
        prof.email = request.POST['email']
        prof.phone = request.POST['phone']
        prof.address = request.POST['address']
        prof.role = request.POST['role']
        prof.desc = request.POST['desc']

        ed.degree1 = request.POST['degree1']
        ed.college1 = request.POST['college1']
        ed.gpa1 = request.POST['gpa1']
        ed.degree2 = request.POST['degree2']
        ed.college2 = request.POST['college2']
        ed.gpa2 = request.POST['gpa2']

        exp.compName1 = request.POST['CompName1']
        exp.compPeriod1 = request.POST['CompPeriod1']
        exp.compRole1 = request.POST['CompRole1']
        exp.compName2 = request.POST['CompName2']
        exp.compPeriod2 = request.POST['CompPeriod2']
        exp.compRole2 = request.POST['CompRole2']

        proj.proj1 = request.POST['Proj1']
        proj.projDesc1 = request.POST['ProjDesc1']
        proj.proj2 = request.POST['Proj2']
        proj.projDesc2 = request.POST['ProjDesc2']

        skills.skills = request.POST['skills']

        interests.interests = request.POST['interest']
        
        prof.save()
        ed.save()
        exp.save()
        proj.save()
        skills.save()
        interests.save()

        return redirect(dashboard)
    
    return render(request, 'updateResume.html', context)



def deleteResume(request, id):
    prof = Profile.objects.get(id=id)
    prof.delete()
    return redirect(dashboard)