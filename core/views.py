from django.shortcuts import render, redirect
from core.models import Tweet
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def splash(request):
    if request.method == "POST":
        print("splash post request")
        body = request.POST["body"]
        print(body)
        Tweet.objects.create(body=body, author=request.user)
    else: 
        print("splash get request")
    # tweets = Tweet.objects.filter(author=req)
    tweets = Tweet.objects.all()
    return render(request, "splash.html", {"tweets" : tweets})

def delete(request):
        tweet = Tweet.objects.get(id=request.GET['id'])
        tweet.delete()

def login_view(request):
    if request.method == "POST":
        print("post request")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("redirecting")
            return redirect("/splash/")
        else: 
            return render(request, 'login.html', {"isValid":False})
    else:
        print("get request")
    return render(request, 'login.html', {"isValid":True})

def logout_view(request):
    logout(request)
    return redirect("/")

def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect('/login/')
    return render(request, 'signup.html', {})