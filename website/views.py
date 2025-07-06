from django.shortcuts import render

def index(requests):
    return render(requests , "website/index.html")
def about(requests):
    return render(requests , "website/about.html")
def contact(requests):
    return render(requests , "website/contact.html")
def post(requests):
    return render(requests , "website/post.html")

# Create your views here.
