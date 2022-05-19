from django.shortcuts import redirect, render
from shop import models

def home(request):
    context = {'pageTitle': 'Home'}
    return render(request, 'home.html',context)

def signup(request):
    def containsDigit(p):
        return True in [c.isdigit() for c in p]
    def containsUpper(p):
        return True in [c.isupper() for c in p]
    def containsLower(p):
        return True in [c.islower() for c in p]
    def containsSpecial(p):
        return True in [not(c.isalnum()) for c in p]

    errors = []
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if len(username) < 3:
            errors.append('Username must be at least 3 characters long')
        if len(password) < 8 and not (containsDigit(password) and containsUpper(password) and containsLower(password) and containsSpecial(password)):
            errors.append('Password must be at least 8 characters long and contain at least one digit, one upper case letter, one lower case letter and one special character')
        if password != confirmPassword:
            errors.append('Passwords do not match')
        
        if len(errors) == 0:
            user = models.Customer(username=username, email=email, password=password)
            user.save()
            print("User created",user)
            return render(request,'home.html',{'pageTitle':'Home'})
    
        if len(errors) == 0:
            print("user created successfully")
            return redirect('home')

    context = {'pageTitle': 'Signup','errors':errors}
    return render(request, 'signup.html',context)

def login(request):
    context = {'pageTitle': 'Login','errors':None}
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = models.Customer.objects.filter(email=email,password=password)
        if user:
            print("Successfully logged in")
            return render(request,'home.html',context)
        else:
            print("Failed to log in")
            context = {'pageTitle': 'Login','errors':['Invalid email or password']}
            return redirect("home")
    return render(request, 'login.html',context)

def listProducts(request):
    context = {'pageTitle': 'Products','products':models.Product.objects.all()}
    return render(request, 'shop.html',context)

def editProfile(request):
    customer = models.Customer.objects.filter(email='ravi@gmail.com')
    user = {'username':customer[0].username, 'email':customer[0].email}
    context = {'pageTitle': 'Edit Profile','user':user}
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        customer = models.Customer.objects.get(email=email)
        customer.username = username
        customer.save()
        print("User updated")
        context = {'pageTitle': 'Home'}
        return redirect("home")

    return render(request, 'editProfile.html',context)