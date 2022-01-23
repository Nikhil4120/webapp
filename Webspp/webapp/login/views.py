from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        loginuser = request.POST['loginuser']
        loginpass = request.POST['loginpass']

        # select * from  User where username=loginuser and password = loginpass
        user = auth.authenticate(username=loginuser, password=loginpass)
        print(user)
        if user is not None:
            # otp = random.randrange(100000, 999999)
            # print(otp)
            request.session['user'] = user.username
            auth.login(request, user)
            return redirect("/")
            # request.session['otp'] = otp
            # context = {'email': user.email, 'otp': otp}
            # mail(context)

            #return render(request, 'otp.html')

        else:
            messages.error(request, "please enter valid credentials")
            return redirect('/')