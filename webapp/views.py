from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products
from.models import Signup 
from.models import Order
from django.contrib.auth import authenticate,login
from .forms import ProductsForm
from.forms import SignupForm 
from.forms import RegisterUserForm
from.forms import OrderForm
from django.contrib.auth.forms import UserCreationForm






def homepage(request):

	return render(request,'project/homepage.html')

def services(request):

	return render(request,'project/services.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST or None)
        if form.is_valid():
           form.save()

        return render(request,'project/successpage.html',{})
        
        
    else:
        return render(request,'project/signup.html',{})
        


def products(request):

    all_data = Products.objects.all
    return render(request, 'project/products.html', {'all': all_data})

def account(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           return render(request,'project/accsuccesspage.html',{})

        else:
           form = RegisterUserForm()
           return render(request,'project/accfailpage.html',{})
     
    else:
        form = RegisterUserForm()
        return render(request,'project/account.html', {'form':form})

      

def loginuser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")

        else:
            print('invalid')
            return redirect("account")
            
    else:
        return render(request,'project/loginuser.html')

def cart(request):
    return render(request,'project/cart.html')


def shipping(request):

    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
           form.save()

        return render(request,'project/ordersuccesspage.html')
        
        
    else:
        return render(request,'project/shipping.html',{})

    return render(request,'project/shipping.html',{})

def successpage(request):
    return render(request,'project/successpage.html')

def ordersuccesspage(request):
    return render(request,'project/ordersuccesspage.html')

def accsuccesspage(request):
    return render(request,'project/accsuccesspage.html')

    
def accfailpage(request):
    return render(request,'project/accfailpage.html')
      
