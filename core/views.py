from django.shortcuts import render, redirect
from core.models import Tweet, Hashtag
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.method == "POST":
        if str(request.user)!="AnonymousUser":
            body = request.POST["body"]
            tweet = Tweet.objects.create(body=body, author=request.user)
            getHashtags(tweet, request)
        else:
            return render(request, "home.html", {"tweets" : tweets, "user": request.user, "valid": False})
    tweets = Tweet.objects.order_by("created_at").reverse()
    return render(request, "home.html", {"tweets" : tweets, "user": request.user, "valid": True})

def about(request):
    return render(request, "about.html", {})

def profile(request):
    if str(request.user)=="AnonymousUser":
        return render(request, "profile.html", {"tweets" : [], "user": request.user, "valid": False})
    tweets = Tweet.objects.filter(author=request.user).order_by("created_at").reverse()
    return render(request, "profile.html", {"tweets" : tweets, "user": request.user, "valid": True})


def getHashtags(t, request):
    #parse hashtags and return an array with hashtags and tweets
    names = [c for c in t.body.split() if c.startswith('#')]
    for name in names:
        hashtag = Hashtag.objects.filter(name=name)
        if hashtag.exists():
            tweets = hashtag[0].tweets
            tweets.add(t)
        else:
            print("add hashtag: " + name)
            h1 = Hashtag(name=name)
            h1.save()
            h1.tweets.add(t)

def parseTweet(text, request):
    parsedText = [] #(text, isHashtag)
    for char in text:
        if char == '#':
            hashName = ''
            while(char != ' '):
                hashName += char
            #get hashtag
            parsedText.append(hashName, True)
        else:
            bodyName = ''
            while(char != ' '):
                bodyName += char
            parsedText.append(body, False)
    return parsedText


def hashtagAll(request):
    hashtags = Hashtag.objects.all()
    return render(request, "hashtag.html", {"hashtags" : hashtags})

def hashtag(request):
    hashtags = Hashtag.objects.get(name=request.GET['name'])
    return render(request, "hashtag.html", {"hashtags" : hashtags})

def delete(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if request.user == tweet.author:
        tweet.delete()
        #check if hashtag exist
        for hashtag in Hashtag.objects.all():
            if not hashtag.tweets.exists():
                hashtag.delete()
    else:
        print("no authorization!")
    return redirect("/home/")

def like(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if request.user not in tweet.likes:
        tweet.likes.add(request.user)
    else:
        tweet.likes.delete(request.user)
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