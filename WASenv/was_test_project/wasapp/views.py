from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def course(request):
    return HttpResponse("If u can see me well done!")