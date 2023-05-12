from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')
def login_page(request):
    return render(request, 'login.html')
def signup_page(request):
    return render(request, 'signup.html')
def home_page(request):
    return render(request, 'homes.html')