from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from board.models import School, Meal


# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello.")
    school_list = School.objects.all()
    # for i in school_list:
    #     str = i.school_name
    #     break
    # return HttpResponse(str)
    context = {'school_list': school_list}
    return render(request, 'board/index.html', context)

def detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    # return HttpResponse(school.school_name)
    return render(request, 'board/detail.html', {'school': school})
