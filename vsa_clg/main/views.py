from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
#forms.py
from .forms import StudentForm
#models 
from .models import Student,Result,Teacher
#user authenticate
from django.contrib.auth.forms import authenticate
from django.contrib.auth import login, logout
# gamil 
from django.core.mail import send_mail
from django.conf import settings
class Home(View):
    def get(self,request):
        try:
            student = Student.objects.get(user = request.user)
            context  = {'data' : student}
            return render(self.request,'home.html',context)
        except Exception as e:
            return render(self.request,'home.html')
class Blog(View):
    def get(self,request):
        return render(self.request,'blog.html')
class About(View):
    def get(self,request):
        return render(self.request,'about.html')
class Service(View):
    def get(self,request):
        return render(self.request,'services.html')
class Contact(View):
    def get(self,request):
        return render(self.request,'contact.html')
    def post(self,request):
        data = request.POST
        name = data['name']
        msg = data['message']
        email = data['email']
        message = msg + 'this email :' + email
        from_email = email
        recipient_list = [settings.EMAIL_HOST_USER]
        subject = f'A User "{name}" tryna contact'
        send_mail(subject,message,from_email,recipient_list)
        return redirect('home')
class Login(View):
    def get(self,request):
        return render(self.request,'login.html')
    def post(self,request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(self.request,'login.html',{'error':'username or password invalid '})
        return redirect('home')

class StudentRegisterUpdate(View):
    def get(self,request,pk):
        data = Student.objects.get(uid=pk)
        if request.user == data.user:
            context = {'data' : data} 
            return render(self.request,'student_reg.html',context)
        else:
            return render(self.request,'nauthorized.html')
    def post(self,request,pk):
        data = request.POST
        usr = Student.objects.get(uid=pk)
        try:
            usr.name = data['sname']
            usr.age = data['age']
            usr.email = data['email']
            usr.phone = data['phone']
            usr.dept = data['dept']
            usr.year = data['year']
            usr.address = data['address']
            usr.dob = data['dob']
            usr.slug = slugify(usr.name)
            usr.save()
            return redirect('home')
        except Exception as e:
            print(f'\n\nerror : {e}\n\n')
            return render(self.request,'student_reg.html',{'error':e})
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
class StudentProfile(View):
    def get(self,request,slug):
        post = get_object_or_404(Student,slug=slug)
        if request.user == post.user or request.user.is_staff:
            context = {'data' : post}
            return render(self.request,'profile.html',context)
        else:
            return render(self.request,'nauthorized.html')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
class Result_view(View):
    def get(self,request):
        data = Result.objects.get(user = request.user)
        return render(self.request,'result.html',{'data' : data})
def Logout(request):
    logout(request)
    return redirect('home')
def custom_404(request, exception):
    return render(request, '404.html', status=404)
    