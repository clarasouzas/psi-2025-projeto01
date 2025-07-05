from django.shortcuts import render

def index(requests):
    return render(requests , "website/index.html")
def about(requests):
    return render(requests , "website/about.html")
def contact(requests):
    return render(requests , "website/contact.html")
def doctor(requests):
    return render(requests , "website/doctor.html")

# Create your views here.
