from django.shortcuts import render, redirect
from core.models import Tweet, Hashtag, TextPair
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.method == "POST":
        if str(request.user)!="AnonymousUser":
            body = request.POST["body"]
            tweet = Tweet.objects.create(body=body, author=request.user)
            parseTweet(tweet, request)
        else:
            tweets = Tweet.objects.order_by("created_at").reverse()
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

def parseTweet(currTweet, request):
    text = currTweet.body
    i = 0
    while i < len(text):
        char = text[i]
        if char == '#':
            hashName = ''
            while(char != ' ' and i < len(text)-1):
                hashName += char
                i+=1
                char = text[i]
            if(char != ' '):
                hashName += char
            parsedText=TextPair.objects.create(text=hashName, isHash=True, belongTo=currTweet)
            currTweet.parsed.add(parsedText)
            #create/modify hashtag
            hashtag = Hashtag.objects.filter(name=hashName)
            if hashtag.exists():
                tweeted = hashtag[0].tweeted
                tweeted.add(currTweet)
            else:
                h1 = Hashtag(name=hashName)
                h1.save()
                h1.tweeted.add(currTweet)
        else:
            bodyName = ''
            while(char != '#' and i < len(text)-1):
                bodyName += char
                i+=1
                char = text[i]
            if(char != '#'):
                bodyName += char
            parsedText = TextPair.objects.create(text=bodyName, isHash=False, belongTo=currTweet)
            currTweet.parsed.add(parsedText)
        if i == len(text)-1:
            break



def hashtagAll(request):
    hashtags = Hashtag.objects.all()
    return render(request, "hashtag.html", {"hashtags" : hashtags})

def hashtag(request):
    print("start")
    name = request.GET.get('name', '')
    if name is '':
        hashtags = Hashtag.objects.all()
        return render(request, "hashtag.html", {"hashtags" : hashtags})
    else:
        wantName = '#' + name
        print("name:" + wantName)
        hashtags = Hashtag.objects.filter(name=wantName)
        if hashtags.exists():
            return render(request, "hashtag.html", {"hashtags" : hashtags})

    

def delete(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if request.user == tweet.author:
        tweet.delete()
        #check if hashtag exist
        for hashtag in Hashtag.objects.all():
            if not hashtag.tweeted.exists():
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
    #check if hashtag exist
        for hashtag in Hashtag.objects.all():
            if not hashtag.tweeted.exists():
                hashtag.delete()
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