from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from home.models import Category,SubCategory

# Create your views here.

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['Firstname']
        lname = request.POST['Lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(pass1)
        print(pass2)
        # select * from User where username = username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist")
            return redirect('/')
        
        if len(username) > 10:
            messages.error(request, "Username must be less than 10 character")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric form")
            return redirect('/')

        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            # context = {'email': email, 'user': username}
            # mail(context)
            messages.success(request, "User Created Successfully")
            return redirect('/')
        else:
            messages.error(request, "Password Does not match")
            return redirect('/')
    else:
        category = Category.objects.all()
        subcategory = SubCategory.objects.all()
        context = {'category': category, 'subcategory': subcategory}
        return render(request,"register.html",context)