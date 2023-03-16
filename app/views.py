from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from profiles.models import Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import loader
from django.urls import reverse

from django.core.mail import EmailMessage
from django.conf import settings

from django.template import loader
from django.urls import reverse
from profiles.models import Profile


# @login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')



def index(request):
  mymembers = Profile.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers
  }
  return HttpResponse(template.render(context, request))


def updated(request,phone):
     mymembers = Profile.objects.get(phone=phone)
     return render(request,'updated.html',{'mymembers':mymembers})

def do_edit(request,phone):
    name=request.POST.get('name')
    email=request.POST.get('email')
    

    mymembers = Profile.objects.get(phone=phone)
    mymembers.name=name
    mymembers.email=email
   
    mymembers.save()

    return redirect('/index')




def delete(request,phone):
    mymembers = Profile.objects.filter(phone=phone).delete()
    return redirect('/index')






def Userss(request):
    n=''
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        
        en=Profile(name=name,email=email,phone=phone)
        en.save()
        email = EmailMessage(
            'Test Email', #subjecr
            f'Hi Threre{name}! \n, Thak your for.{phone} the mas: \n \n {email} \n \n http://127.0.0.1:8000/updated/{phone}', #mess
            settings.EMAIL_HOST_USER, #sender
            [email] #resiver
        )

        email.fail_silently =True
        email.send()
        n='submited'
        return redirect('index')

    return render(request,'signup.html',{'n':n})



def RegiLPage(request):
    pass

def Login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passs1=request.POST.get('pass')
        user=authenticate(request,email=email,password1=passs1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("user name n apss incorrect")  


    return render(request,'login.html')

    
def LogoutPage(request):
    logout(request)
    return redirect('login')









# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
# def HomePage(request):
#     return render(request,'home.html')

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('name')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
#         if pass1!=pass2:
#             return HttpResponse("your password n confirm  pass same")
#         else:

#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')



         
#     return render(request,'signup.html')

# def LoginPage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         passs1=request.POST.get('pass')
#         user=authenticate(request,username=username,password=passs1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse("user name n apss incorrect")  


#     return render(request,'login.html')


# def LogoutPage(request):
#     logout(request)
#     return redirect('login')





# # Create your views here.
