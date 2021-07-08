from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Category
from user.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.forms import SignUpForm

# Create your views here.

def indes(request):
    return HttpResponse("'User App'")

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Algo se ingresó incorrectamente, hagámoslo nuevamente:)")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.

    category = Category.objects.all()
    context = {'category': category
     }
    return render(request, 'user/login_form.html',context)

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.save()
            messages.success(request, 'Tu cuenta ha sido creada!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')


    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'user/signup_form.html', context)


