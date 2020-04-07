from django.shortcuts import render
from core.models import Tweet
# Create your views here.
def splash(request):
	tweets = Tweet.objects.all()
	return render(request, "splash.html", {"tweets" : tweets})