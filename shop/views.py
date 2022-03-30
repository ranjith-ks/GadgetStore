from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from shop import models

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        user = models.User(username=username, email=email, password=password)
        user.save()
        print("User created",user)
        return render(request,'home.html')
    return render(request, 'signup.html')

def addProduct(request):
    if request.method=='GET':
        return render(request, 'add-product.html')
    if request.method=='POST':
        productName = request.POST['productname']
        productURL = request.POST['producturl']
        productPrice = request.POST['price']
        productDiscount = request.POST['discount']
        productDescription = request.POST['description']
        product = models.Product(productName=productName,productURL=productURL, productPrice=productPrice,productDiscount=productDiscount, productDescription=productDescription)
        product.save()
        print("Product created",product)
    return render(request,'home.html')