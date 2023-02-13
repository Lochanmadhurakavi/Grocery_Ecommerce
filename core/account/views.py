from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'account/signup.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('/')


