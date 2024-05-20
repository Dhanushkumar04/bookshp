from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required
from Bookstore.urls import *

# Create your views here.

def login(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request,f'Invalid login')
            return redirect("login")
    else:        
        return render(request, "login.html")


def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            if password == cpassword:
                user = User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            else :
                return redirect('signup')   
        else:
            return render(request, "signup.html")
    except:
        messages.info(request, "Username is already exists.")
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)    
    return redirect('home')

def home(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        count = cart_items.count()
        return render(request, 'home.html', {'products': products, 'count':count})
    return render(request, 'home.html', {'products': products})
 
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    count = cart_items.count()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'count': count})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("view_cart")

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect("view_cart")

def view_desc(request):
    return render(request,'description.html')



    


