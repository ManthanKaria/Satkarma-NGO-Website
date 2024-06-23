from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.urls import path
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# from django.shortcuts import render, redirect
from django.contrib import messages
# from django.core.exceptions import ObjectDoesNotExist
# from .models import Student
# import Users

# Create your views here.

def index(request):
    return render(request, 'index.html')

# def book_registration(request):
#     if request.method =='POST':
#         uname=request.POST.get('username')
#         name=request.POST.get('fname')
#         email=request.POST.get('email')
#         phone=request.POST.get('phone')
#         pass1=request.POST.get('pass1')
#         pass2=request.POST.get('pass2')
#         gender=request.POST.get('gender')
#         school=request.POST.get('school')
#         dob=request.POST.get('dob')
#         upload = request.POST.get('upload')
#         result = request.FILES.get('result')
#         document = request.FILES.get('document')

#         if (pass1!=pass2):
#                 msg = "Password error"
#                 return render(request, "book_registration.html",{'msg':msg})

#         try:
#             existing_student = Student.objects.get(phone=phone)
#             msg = "A user with this phone number already exists."
#             return render(request, "book_registration.html", {'msg': msg})
#         except Student.DoesNotExist:
#             pass 

#         try:
#             existing_student1 = Student.objects.get(username=uname)
#             msg = "A user with this Username already exists."
#             return render(request, "book_registration.html", {'msg': msg})
#         except ObjectDoesNotExist:
#             pass 


#         my_user = Student.objects.create(username=uname, name=name, gender=gender, email=email, school=school, date=dob,
#                                             phone=phone, upload=upload, documents=document, result=result, confirm_password=pass2, password=pass1)
#         my_user.save()
#         return redirect("login")
#     return render(request, 'book_registration.html')



def book_registration(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        gender = request.POST.get('gender')
        school = request.POST.get('school')
        dob = request.POST.get('dob')
        upload = request.POST.get('upload')
        result = request.FILES.get('result')
        document = request.FILES.get('document')

        if pass1 != pass2:
            msg = "Password error"
            return render(request, "book_registration.html", {'msg': msg})

        try:
            existing_student = Student.objects.get(phone=phone)
            msg = "A user with this phone number already exists."
            return render(request, "book_registration.html", {'msg': msg})
        except Student.DoesNotExist:
            pass 

        try:
            existing_student1 = Student.objects.get(username=uname)
            msg = "A user with this Username already exists."
            # Store the message in the session
            request.session['user_exists_message'] = msg
            return render(request, "book_registration.html", {'msg': msg})
        except ObjectDoesNotExist:
            pass 

        my_user = Student.objects.create(
            username=uname, name=name, gender=gender, email=email, school=school, date=dob,
            phone=phone, upload=upload, documents=document, result=result, confirm_password=pass2, password=pass1
        )
        my_user.save()
        return redirect("login")

    # Clear the message if it exists in the session
    if 'user_exists_message' in request.session:
        del request.session['user_exists_message']

    return render(request, 'book_registration.html')


def login(request):
    return render(request, 'login.html')

def shope(request):
    return render(request, 'shope.html')

def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # checking
        # user = Student.objects.get(username=username)

        # if user not exist
        try:
            user = Student.objects.get(username=username)
        except ObjectDoesNotExist:
            msg = "User does not exist"
            return render(request, "login.html", {'msg': msg})

        # password verification
        if user.password == password:
            request.session['username']=user.username; 
            request.session['phone']=user.phone; 
            request.session['email']=user.email; 
            request.session['name']=user.name; 
            return redirect('showing')
            # return render(request,'index.html')
        else:
            msg = "Password is not match"
            return render(request, "login.html",{'msg':msg})   
        # else:
        #         msg = "User Not Exist"
        #         return render(request, "book_registration.html",{'msg':msg})


def CartView(request):
    return render(request,"cart.html")

# image fetch
def ImageFetch(request):
    all_img = Product.objects.all() 
    return render(request,"shop.html",{'key1':all_img})

# add to cart
# def Add_To_Cart(request):
#     product = request.POST.get('add_to_cart')
#     print(product)
    
# def Add_To_Cart(request):
#     product = request.POST.get('add_to_cart')
#     # Assuming 'shop' is your session key for the cart items
#     if 'shop' not in request.session:
#         request.session['shop'] = {}
#     request.session['shop'][product] = request.session['shop'].get(product, 0) + 1
#     request.session.modified = True  # Ensure session is saved
#     print(request.session['shop'])  # For testing, you can remove this line later
#     return redirect('cartview') 





# GFG code
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')