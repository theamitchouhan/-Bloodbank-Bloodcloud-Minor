from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'home/home.html')
    # return HttpResponse("This is homepage")