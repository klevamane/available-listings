from django.shortcuts import render, redirect, resolve_url

# Create your views here.


def signup(request):
    """The signup function, enables a user to register a new account"""
    # current_url = resolve_url(request.path_info)
    if request.method == 'POST':
        return redirect('signup')
    return render(request, 'accounts/signup.html')


def signin(request):
    """The signin function allows an already registered user access the application

    The user should be able to access the application restricted endpoints provided
    the user enters a matching combination of email and password
    """
    if request.method == 'POST':
        return redirect('signin')
    return render(request, 'accounts/signin.html')


def signout(request):
    """This function enable a user logout of the application"""

    return redirect('index')


def dashboard(request):

    return render(request, 'accounts/dashboard.html')


