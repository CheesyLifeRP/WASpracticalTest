from django.http import HttpResponse
from django.shortcuts import render
from wasapp.models import Category

# Create your views here.
def course(request):
    course_list = Category.objects.all()

    context_dict = {}
    context_dict['courses'] = course_list
    return render(request, 'was_test/was.html', context=context_dict)
