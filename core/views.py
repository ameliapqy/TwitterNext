from django.shortcuts import render, redirect
from core.models import Tweet
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.method == "POST":
        if str(request.user)!="AnonymousUser":
            body = request.POST["body"]
            Tweet.objects.create(body=body, author=request.user)
        else:
            return render(request, "home.html", {"tweets" : tweets, "user": request.user, "valid": False})
    tweets = Tweet.objects.order_by("created_at").reverse()
    return render(request, "home.html", {"tweets" : tweets, "user": request.user, "valid": True})

def about(request):
    return render(request, "about.html", {})

def profile(request):
    if request.method == "POST":
        body = request.POST["body"]
        Tweet.objects.create(body=body, author=request.user)
    tweets = Tweet.objects.order_by("created_at").reverse()
    return render(request, "profile.html", {"tweets" : tweets})

def hashtag(request):
    hashtag = Hashtag.objects.get(name=request.GET['name'])
    return render(request, "profile.html", {"hashtag" : hashtag})

def delete(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if request.user == tweet.author:
        tweet.delete()
    else:
        print("no authorization!")
    return redirect("/home/")

def deletep(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if request.user == tweet.author:
        tweet.delete()
    else:
        print("no authorization!")
    return redirect("/profile/")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home/")
        else: 
            return render(request, 'login.html', {"isValid":False})
    return render(request, 'login.html', {"isValid":True})

def logout_view(request):
    logout(request)
    return redirect("/login/")

def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect('/login/')
    return render(request, 'signup.html', {})