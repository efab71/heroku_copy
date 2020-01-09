from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status


from .models import Greeting
from .models import Main
from hello.serializers import MainSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content=JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

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

@csrf_exempt
def drivers(request):
    
    if request.method == 'GET':
        drivers=Main.objects.all()
        drivers_serializer=MainSerializer(drivers, many=True)
        return JSONResponse(drivers_serializer.data)
    
    elif request.method=='POST':
        drivers_data = JSONParser().parse(request)
        drivers_serializer=MainSerializer(data=drivers_data)
        if drivers_serializer.is_valid():
            drivers_serializer.save()
            return JSONResponse(drivers_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(drivers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

        