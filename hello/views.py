from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

@csrf_exempt
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

@csrf_exempt
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
