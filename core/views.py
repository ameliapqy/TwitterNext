from django.shortcuts import render
from core.models import Tweet
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def splash(request):
    if request.method is "POST":
        print(request.POST["title"], request.POST["body"])
        body = request.POST["body"]
        Tweet.objects.create(body=body, author=request.user)
    # tweets = Tweet.objects.filter(author=req
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
            print("redirected")
            return redirect("/")
    return render(request, 'accounts.html', {})

def logout_view(request):
    logout(request)
    return redirect("/login")

def signup_view(request):
	user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
	login(request, user)
	return redirect('/')