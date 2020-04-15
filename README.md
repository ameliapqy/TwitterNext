# TwitterNext

![](TwitterNext.mp4)

TwitterNext is an individual project that is a website with Twitter’s functionality and a futuristic look. Visitors can create an account, sign in, create tweets that support hashtagging, delete tweets, and have an individual profile page. Django is used for the main framework.

## Getting Started

### Prerequisites

have Python3 installed 

### Installing

navigate to the project folder in terminal and type the following to run the website.

```
python3 manage.py runserver
```

## Pages & Functionalities

###Login/Signup

Visitors can create accounts in /signup page, which can be redirected from the initial login page. Log in by entering username and password.

###Home

After logging in, user enters the /home page where one could see all the tweets. User can send a tweet with or without hashtags. 
Lastest tweets are displayed on top, with user and time tweeted in the header.
A user can like and unlike tweet using ♥ , and the number next to ♥ shows how many times the tweet is liked by unique users. 
A user can also delete the tweet one wrote, but can't delete other user's tweets. 

*you can also enter /home unregistered, but you can't tweet or like any tweets*

###About/Splash

/About page has an explanation of product and concept. 

###Hashtag

All tweets support hashtags, and if the user clicks the hashtag within a tweet, it will redirect to the hashtag page where it contains the specific hashtag clicked.

/hashtag page contains all hashtags with corresponding tweets below. A tweet can have multiple hashtags

###Profile

/Profile page shows all tweets the current user tweeted, and all tweets can be deleted on this page. 

## Design 

Bootstrap and custom CSS is used to give the website a lightweight and futuristic feel. 

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - The CSS framework used
