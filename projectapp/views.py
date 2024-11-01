from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username already exists')
                return render(request, 'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email already exists')
                return render( request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, )
                user.save()
                messages.success(request, 'Your acount has been created successfully.')
                return redirect('signin')
        else:
            messages.error(request, 'Unmatched passwords')
            return redirect('signup.html')
    else:
        return render(request, 'signup.html')


def signin(request): 
    if request.method == 'POST':
        username = request.POST['loginname']
        password = request.POST['loginpassword']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect( 'main')
        else:
            messages.error(request, 'Incorrect credentials')
            return render(request, 'signin.html')

    else:
            
        return render(request, 'signin.html')


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def category(request):
    return render(request, 'category.html')


def contact(request):
    return render(request,  'contact.html')


def single_post(request):
    return render(request, 'single-post.html')


def signout(request):
    logout(request)
    return redirect('main')


def dashboard(request):
    return render(request, 'dashboard.html')

def extend_signup(request):
    return render(request, 'main.html')

