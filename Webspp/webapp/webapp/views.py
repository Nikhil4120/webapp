from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from home.models import Category,SubCategory,Product


def home(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    context= {'category':category,'subcategory':subcategory}
    return render(request,'index.html',context)

def forget(request):
    if request.method == "POST":
        email = request.POST['emailid']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if(User.objects.filter(email=email)).exists():
            if(password == cpassword):
                messages.success(request,"Password Change Successfully")
                u = User.objects.get(email=email)
                u.set_password(password)
                u.save()
                return redirect('/')
            else:
                messages.error(request,"Password Doesnot match")
                return redirect('/')
        else:
            messages.error(request,"emailid not exist")
            return redirect('/')


    else:
        return render(request,'forget.html')