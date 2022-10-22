from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from formapp.models import Form


def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['conform_password']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Id already exists")

                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)

                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password not matching")
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return redirect('/')
            return redirect('reg_form')
            # messages.info(request, "Successfull Login")

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')


def reg_form(request):
    return render(request, 'reg_form.html')
def add_form(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        dob= request.POST.get('dob', )
        gender=request.POST.get(' gender',)
        number=request.POST.get('number',)
        address= request.POST.get('address', )
        email = request.POST.get(' email', )
        district = request.POST.get('district', )
        branches = request.POST.get('branches', )
        account = request.POST.get(' account', )
        materialsprovided= request.POST.get('materialsprovided', )

        f=Form(name=name,dob=dob,gender=gender,number=number,
               address=address,email=email,district=district,
               branches=branches,account=account,materialsprovided=materialsprovided)
        f.save()
        return redirect('submit')
    return render(request,'form.html')
def submit(request):
    f = Form.objects.all()
    context = {
        'f': f
    }
    return render(request, 'submit.html', context)
def logout(request):
    auth.logout(request)
    return redirect('/')